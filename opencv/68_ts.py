
## Tesseract
# 광학 문자 인식(OCR) 라이브러리
# 독일 만하임 대학교 사이트에서 다운로드(https://github.com/UB-Mannheim/tesseract/wiki)
# Tesseract 설치 후 pip install pytesseract 명령하기


import sys
import random
import numpy as np
import cv2
# import pytesseract


def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환한다.
    print('인덱스 : ', idx)
    
    # x 좌표 큰순으로 오름차순 정렬
    pts = pts[idx] # [1 0 2 3]   
    print(pts)  
    '''
    [[226. 322.]
     [320. 112.]
     [713. 416.]
     [755. 174.]]
    '''
    
    # y좌표값 비교 후 바꿈
    # 반시계 방향으로 정렬된 좌표 pts 구하기
    if pts[0, 1] > pts[1, 1]:
        # 322. > 112. 을 비교
        pts[[0, 1]] = pts[[1, 0]]
        '''
        [[226. 322.]
         [320. 112.]] 
         pts의 첫번째, 두번째 인덱스 값을 서로 바꿈
        '''

    if pts[2, 1] < pts[3, 1]:
        # 416. > 174. 을 비교
        pts[[2, 3]] = pts[[3, 2]]

    print(pts)
    '''
    [[320. 112.]
    [226. 322.]
    [713. 416.]
    [755. 174.]]
    '''
    return pts 

# 영상 불러오기
filename = './images/name_card_3.jpg'

if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv2.imread(filename)

if src is None:
    print('Image load failed!')
    sys.exit()

dw, dh = 720, 400

srcCoord = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstCoord = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)


# 새로운 프레임 하나 생성
dst = np.zeros((dh, dw), np.uint8)

# 영상 이진화
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 검출
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 원본 영상 복사
cpy = src.copy()
for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue # 노이즈 패스

    # 외곽선 근사화
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    if not cv2.isContourConvex(approx) or len(approx) != 4:
        continue # 컨벡스가 아니거나 꼭지점이 4개가 아닌것을 패스

    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    # print(approx) # 3차원
    srcCoord = reorderPts(approx.reshape(4, 2).astype(np.float32)) # 명함 모서리 4개의 좌표값
    # print(srcCoord) # 2차원


# 투시변환을 이용해서 영상 펴기
pers = cv2.getPerspectiveTransform(srcCoord, dstCoord)
dst = cv2.warpPerspective(src, pers, (dw, dh))

dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
# 이미지에 있는 글씨(한글,영어)를 문자열로 가져오기
# print(pytesseract.image_to_string(dst_gray, lang="Hangul+eng"))



cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
