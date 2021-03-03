
####################### 이미지 히스토그램 스트레칭하기 ######################

import sys, cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("./images/river.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("failed")
    sys.exit()


def getHistDraw(hist):
    imgHist = np.full((100,256), 255, dtype=np.uint8) # 흰색배경의 행렬 생성 
    print(hist.shape)
    histMax = np.max(hist)
    
    for x in range(256):
        pt1 = (x, 100)   # 시작점, 히스토그램 좌측 상단 기준
        pt2 = (x, 100 - int(hist[x,0]*100/histMax)) # 끝점, 100을 곱하고 255로 나눠 단위 통일
        cv2.line(imgHist, pt1, pt2, 0) # 직선을 그려 히스토그램 그리기
    
    return imgHist

## cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)
# src: 입력 영상
# dst: 결과 영상 (None 입력)
# alpha: (노름 정규화인 경우) 목표 노름 값, (원소 값 범위 정규화인 경우) 최솟값
# beta: (원소 값 범위 정규화인 경우) 최댓값
# norm_type: 정규화 타입. NORM_INF, NORM_L1, NORM_L2, NORM_MINMAX(히스토그램 스트레칭은 NORM_MINMAX)
# dtype: 결과 영상의 타입
# mask: 마스크 영상


# 스트레칭 
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)  

# 평활화
equal = cv2.equalizeHist(src)


## 히스토그램 구하기(스트레칭과 평활화된 이미지 비교하기)
# 원본의 히스토그램
src_hist = cv2.calcHist([src], [0], None, [256], [0,256]) # 막대 간의 간격을 알 수 없다
src_chart = getHistDraw(src_hist)

# 스트레칭한 이미지의 히스토그램
dst_hist = cv2.calcHist([dst], [0], None, [256], [0,256])
dst_chart = getHistDraw(dst_hist)

# 평활화한 이미지의 히스토그램
equal_hist = cv2.calcHist([equal], [0], None, [256], [0,256])
equal_chart = getHistDraw(equal_hist)

# cv2.imshow("src", src)
# cv2.imshow("dst", dst)


# 히스토그램과 해당 이미지 출력
cv2.imshow("src_chart", src_chart)
cv2.imshow("dst_chart", dst_chart) # 벌어진 간격이 일정함 
cv2.imshow("equal_chart", equal_chart) # 벌어진 간격이 일정하지 않으며, 명암비가 극대화 됨

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("equal", equal)


cv2.waitKey()
cv2.destroyAllWindows()


