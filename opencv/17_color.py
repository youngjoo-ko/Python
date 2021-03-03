# 컬러 space 

### 색 분리(채널 분리)
## cv2.split(.,mv)
# cv2. 다 채널영상(bgr)로 주성된 파일 컬러
# m : 다채널 영상(bgr)로 구성된 컬러영상
# mv : 출력 영상
# dst : 출력영상 리스트

### 색결합(채널결합)
## cv2.merge(mv, dst)
# mv : 입력영상 리스트
# dst : 출력 영상

#### 영상 처리에서는 특정 목적에 따라서 RGB 색 공간(SPACE)을 
# HSV, YCrCb, Grayscale로 전환해서 처리한다

## HSV
# Hue : 색의 종류 (무지개 색깔) 0 ~ 179 까지 표현
# Saturation : 채도(색의 선명도) 0 ~ 255 까지
# Value : 명도(빛의 밝기) 0 ~ 255 까지
# cv2.CV_8U일때  HSV 값의 범위 : 0 <= H <= 179 , 0 <= S,V <= 255

## YCrCb : PAL(유럽 방송주파수 방식), NTSC(미국,한국 방송주파수 방식) 등의 컬러비디오 표준에 사용되는 색공간
# Y : 밝기 정보(luma)
# Cr, Cb : 색차(chroma)
# cv2.CV_8U일때  YCrCb값의 범위 : 0 < Y , Cr, Cb <= 255

import sys, cv2
import numpy as np


src1= cv2.imread("./images/mnm.png")

if src1 is None:
    print("failed")

# print(src1.shape)
# print(src1.dtype)

# ################## 색 분할 ##################
# b ,g, r = cv2.split(src1) 

# cv2.imshow("src1", src1)
# cv2.imshow("b", b) # 블루만 하얀색
# cv2.imshow("g", g) # 그린, 노란(그린+블루)만 하얀색
# cv2.imshow("r", r) # 레드, 주황, 노랑만  하얀색 (빨간색이 혼합된 색은 전부)

# cv2.waitKey()

########### 색 공간 변환 #################
## cv2.cvtColor(src, code, dst, dstCn) -> dst 교재 75쪽 참고
# src: 입력영상, code: 색변환코드, dst: 출력영상, dstCn: 결과영상의 채널수

## HSV로 변환하기 (hue saturation value)
src_hsv = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)
channel = cv2.split(src_hsv) # 채널수가 2개이상이면 리스트로 받아옴

cv2.imshow("src1", src1)
cv2.imshow("channel[0]", channel[0])
cv2.imshow("channel[1]", channel[1])
cv2.imshow("channel[2]", channel[2])
cv2.waitKey()
