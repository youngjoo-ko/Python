

### 모폴로지 침식 연산 함수
## cv2.erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
# src : 입력영상
# kernel : 구조요소(structuring element), 마스크(필터), 기본값 3x3 
#- kernel 생성함수 : getStructuringElement()에 의해 생성
# anchor : 고정점 위치, 기본값(-1, -1)을 이용하면 자동으로 중앙점이 설정됨
# iterations : 반복횟수, 기본값은 1
# borderType : 가장자리 픽셀 확장방식, 기본값은 cv2.BORDER_CONSTANT
# borderValue : cv2.BORDER_CONSTANT가 설정된 경우, 확장된 가장자리 픽셀을 채울 값

### 모폴로지 팽창 연산 함수
## cv2.dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
# erode와 파라미터는 같다

### 모폴로지 구조 요소(kernel)를 생성하는 함수
## cv2.getStructuringElement(shape, ksize, anchor=None) -> retval
# shape : 커널의 모양을 표현하는 플래그 설정
#- cv2.MORPH_RECT : 사각형(일반적으로 사용)
#- cv2.MORPH_CROSS : 십자가
#- cv2.MORPH_ELLIPSE : 원에 내접한 사각형(특별한 경우에 사용)
# ksize : 커널의 크기(width,height) 튜플로 표현
# anchor : (-1, -1)
## retval : numpy.ndarray(0과 1로 구성된 값, 1의 위치가 커널의 모양을 결정함, 타입은 cv2.CV_8U)

import sys, cv2, numpy as np


src = cv2.imread("./images/circuit.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("lmage load failed!")
    sys.exit()


# 커널 생성
# kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))
# kernel1로 팽창하면 회로가 이어지긴 하나 굵어진다. 이를 해결하려면?
# 커널의 크기 수정(특별한 경우에 해당)
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6))

# 침식
dst1 = cv2.erode(src, kernel2)

# 팽창
dst2 = cv2.dilate(src, kernel2)


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()