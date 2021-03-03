

###################### 3*3 으로 mean filtering 하기 ##############################


## 기본적인 2d 필터링 함수
# cv2.filter2D(src, ddepth, kernel, dsr, anchor, delta, borderType)
# src : 입력영상
# ddept : 출력영상 데이터타입(cv2.CV_8U, cv2.CV_32F, cv2.CV_64F) 
# 필터링 처리에는 float 타입의 데이터가 필요하다
# 그 이유는 영상처리에서 아주 사소한(미미한) 영상의 픽셀 값들을 uint로 하면 결과값이 달라질 수 있다
# kernel : 필터 마스크 행렬(실수형)
# anchor: 고정점, 고정점이 (-1, -1)  이면 중앙점을 anchor로 사용하겠단 뜻 
# 3*3 인경우 1,1이 중앙점이 맞지만, -1,-1로 넣어도 된다
# delta : 추가적으로 더할 값
# borderType : 가장자리 픽셀을 확장하는 방식

import sys, cv2, numpy as np 

src = cv2.imread("./images/rose.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("failed")
    sys.exit()


### 블러처리 방법 2가지    

## 1. cv2.filter2D 함수 사용
# 평균 필터 만들기(마스크 행렬)
# kernel = np.array([[1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9]], dtype= np.float32)

kernel = np.ones((3,3), dtype=np.float64)/9. # 이코드는 위와 같다

# dst = cv2.filter2D(src, -1, kernel) # -1은 입력영상과 동일한 타입으로 만들겠다는 의미

## 2. cv2.blur(src, ksize) 사용 ksize는 평균 필터 크기(weight, height) 튜플 형태
dst = cv2.blur(src, (3,3)) # 위 코드와 결과는 같음, kernel = np.ones((3,3), dtype=np.float64)/9. 을 자동으로 처리함

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
