
## 어파인 변환 행렬 구하는 함수
# cv2.getAffineTransform(src, dst) : 리턴값은 2*3 행렬

## 투시변환 행렬 구하기
# cv2.getPerspectiveTransform(src, dst) : 리턴값은 3*3 행렬

## 어파인 변환함수
# cv2.warpAffine(src, M, dsize, dst, flag, borderMode, borderValue) 

## 투시 변환함수
# cv2.warpPerspective(src, M, dsize, dst, flag, borderMode, borderValue) 
# • src: 입력 영상
# • M: 3x3 투시 변환 행렬. 실수형.
# • dsize: 결과 영상 크기. (w, h) 튜플. (0, 0)이면 src와 같은 크기로 설정
# • dst: 출력 영상
# • flags: 보간법. 기본값은 cv2.INTER_LINEAR
# • borderMode: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT
# • borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.


import sys,cv2, numpy as np

src = cv2.imread('./images/name_card.jpg')
src2 = cv2.imread('./images/soslab.jpg')

if src is None:
    print('Image load failed')
    sys.exit()


# 일반 명함카드 비율 (9:5)
w, h = 720, 400
# w, h = src2.shape[:2]

# 소스의 좌표
# 포토샵 창->정보 - 픽셀값x
# 편집 -> 환경설정 -> 단위와 눈금자 -> 눈금자를 픽셀로 변경
# src_Coord = np.array([[228,115],[797,223],[747,563],[78,382]], dtype=np.float32)
src_Coord = np.array([[143,280],[318,146],[693,337],[566,536]], dtype=np.float32)

# 출력 좌표
dst_Coord = np.array([[0,0],[w,0],[w,h],[0,h]], dtype=np.float32)

# 투시변환행렬
per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)

dst = cv2.warpPerspective(src2, per_matrix, (w,h), 255)

cv2.imshow('src',src2)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()
