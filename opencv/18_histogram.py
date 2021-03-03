

### 히스토그램 : 영상의 픽셀값 분포를 그래프 형태로 표현한 것 
# 포토샵 상단 > 이미지 > 조정 > 레벨 에서 확인 가능
# 0 은 블랙, 255는 화이트 : 이미지에 들어있는 색상에 따라 분포가 다르게 나타난다
# 이미지 > 조정 > 명도 / 대비에서 대비를 주면 선명해지고, 줄이면 탁해진다
# 대비를 많이 줬을때 히스토그램은 0과 255쪽 양쪽으로 쭉 늘어난다.

## 히스토그램 스트레칭 (histogram stretching) 과 평활화(histogram equalization)
# : 영상의 히스토그램이 그레이스케일 전반에 걸쳐 분포되도록 변경하는 선형 변환 기법으로 명암비를 향상시킨다.
# 각 막대들의 간격이 균일하면 histogram stretching , 그렇지 않으면 histogram equalization 이라고 한다
# 두 기능 다 이미지가 선명해지는 효과를 준다.(대비가 커지는!)

# 정규화 함수 (스트레칭)
# cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)

# 평활화 함수 (평활화)
# cv2.equalizeHist(src, dst) => dst
# src : 입력영상, 그레이스케일 영상

## 개념 정리
# contrast : 명암비, 대비 (어두운곳, 밝은곳의 밝기 차이)


### 히스토그램 그리는 함수
## cv2.calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate)
# images : 입력영상 리스트
# channels : 히스토그램을 계산할 채널 번호를 갖는 정수형 배열
# mask : 마스크 영상
# histSize : bin(막대)의 개수
# ranges : 히스토그램 각 차원의 최소, 최대값으로 구성된 리스트
# hist : 계산된 히스토그램
# accumulate : 기존의 hist 히스토그램에 누적여부(True/False)

import sys, cv2
import numpy as np
import matplotlib.pyplot as plt

## 흑백 영상 히스토그램
# src = cv2.imread("./images/woman.bmp", cv2.IMREAD_GRAYSCALE)
# gray_hist = cv2.calcHist([src], [0], None, [256], [0,256]) # 반드시 리스트 형태로 넣어줘야 함!
# cv2.imshow("src", src)
# plt.plot(gray_hist)
# plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()

# ## 컬러 영상 히스토그램
src = cv2.imread('./images/woman.bmp')

if src is None:
    print('Image load failed')
    sys.exit()

# 컬러를 구분할 수 있는 리스트 필요!!!!!!
colors = [ 'b','g','r' ] # -> 각각의 채널에 해당되는 히스토그램을 만들어야 함.
bgr_channels = cv2.split(src)


'''
# zip() 
>>> a = [1,2,3]
>>> b = ['k','o','p']
>>> a_b = list(zip(a,b))
>>> print(a_b)
[(1, 'k'),(2, 'o'),(3, 'p')] 
-> 이런 식으로 값을 같이 받아와서 각각 channel과 c에 대입해준다.
'''

for (channel, c) in zip(bgr_channels, colors):
    color_hist = cv2.calcHist([channel], [0], None, [256], [0,256]) # 각 채널별로 히스토그램
    # hist 타입 : 1차원 행렬
    plt.plot(color_hist, color = c)

cv2.imshow('src',src)
cv2.waitKey(1)

plt.show()

cv2.destroyAllWindows()


plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
