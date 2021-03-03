
######################## inRange() 함수를 이용하여 특정 영역의 컬러 추출하기 ###########################

### 특정 영역안에 있는 컬러를 추출하는 함수 
## cv2.inRange(src, lowerb, upperb, dst)
# lowerb : 영역의 최소값, 행렬이나 스칼라를 입력한다
# upperb : 영역의 최대값, 행렬이나 스칼라를 입력한다

import sys, cv2, numpy as np

src = cv2.imread('./images/mnm.png')
src2 =  cv2.imread('./images/mnm_dark.png')


if src is None:
    print("Image load failed")
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0,128,0), (100,255,100))
# b는 0~100까지, g는 128~255까지, r은 0~100까지의 영역에 있는 컬러만 추출
# RGB 좌표 참고 (3차원 영역)

dst2 = cv2.inRange(src_hsv, (50,150,0), (80,255,255))
# HSV 순서, S 는 채도이므로 위에 RGB와 비슷한 색상을 꺼내오려면 높게 잡아야함, 밝기(E)는 상관없음
# H는 HUE 원색상표 참고

dst3 = cv2.inRange(src2, (0,128,0), (100,255,100)) # 어두운 이미지에서 rgb로 가져왔을때


cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
# 결과만 따지면 RGB로 색상을 추출한 결과값이 더 깔끔하다.
# 근데 영상처리할때 HSV를 쓰는 이유는? 빛의 영향을 받지 않고 고유의 색상을 가져올 수 있기때문(범위를 0~255로 정할 수 있으므로)
# RGB는 어두워지면 색상을 가져오기 힘들다 (dst3)

