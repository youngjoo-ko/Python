

### adaptiveThreshold 함수를 이용한 지역 이진화
# - 수동분할하는 오츠연산을 이 함수로 자동연산해주는 것
## adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst)
# src : 그레이스케일 영상(입력)
# maxValue : 255 (일반적)
# adaptiveMethod : 블록 평균 계산방법(블러) 지정
#- cv2.ADAPTIVE_THRESH_MEAN_C(평균)
#- cv2.ADAPTIVE_THRESH_GAUSSIAN_C(가중치 평균)
# thresholdType : 바이너리 , 바이너리 인버젼 둘 중 하나 선택
# blockSize : 해당 블럭의 크기(보통 3이상의 홀수로 지정)
# C: 블록 내 평균값 또는 블록 내 가중 평균값에서 뺄 값. (x, y) 픽셀의 임계값으로 𝑇(𝑥, 𝑦) = 𝜇(𝑥, 𝑦 )− 𝐶 를 사용

import sys, cv2, numpy as np


src = cv2.imread("./images/sudoku.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("lmage load failed!")
    sys.exit()

def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize - 1
    if bsize < 3:
        bsize = 3

    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bsize, 5) 

    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv2.setTrackbarPos('Block Size', 'dst', 11)
cv2.waitKey()
cv2.destroyAllWindows()