
################################### 히스토그램 평활화 #########################################

import sys, cv2
import numpy as np


# 그레이 스케일 영상의 히스토그램 평활화
# src = cv2.imread("./images/river.jpg", cv2.IMREAD_GRAYSCALE)
# dst = cv2.equalizeHist(src)

# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey()


# 컬러 영상의 히스토그램 평활화
# r,g,b 각각 분리 후 각각 평활화 시키고 다시 합해야 함, 복잡하고 색상성분이 변한다
# YCrCb 의 Y 값만 평활화 시키는 간단한 방법을 사용함


src = cv2.imread("./images/river.jpg")

# YCrCb 로 변환
src_YCrCb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 밝기성분에 대해서만 평활화하기 
channel = cv2.split(src_YCrCb) # 채널 분리
channel[0] = cv2.equalizeHist(channel[0]) # 밝기(y)만 평활화

# 채널 병합하여 다시 원본처럼 bgr로 변환하기
src_merge = cv2.merge(channel) # 색채널 병합
src_bgr = cv2.cvtColor(src_merge, cv2.COLOR_YCrCb2BGR) # 다시 BGR로 변환

# rgb로 해보기
src_rgb = cv2.cvtColor(src_merge, cv2.COLOR_BGR2RGB)

cv2.imshow("src", src)
cv2.imshow("src_merge", src_merge)
cv2.imshow("src_bgr", src_bgr)
cv2.imshow("src_rgb", src_rgb)
cv2.waitKey()

cv2.destroyAllWindows()

