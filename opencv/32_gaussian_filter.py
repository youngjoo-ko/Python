

###################### gaussian filtering 하기 ##############################
## cv2.GaussianBlur(src, ksize, sigmaX, dst, sigmaY, borderType)
# src : 입력영상
# ksize : 가우시안 커널크기(0,0으로 설정하면 sigmaX값에 의해 자동으로 결정됨)
# sigmaX : x방향의 표준편차
# sigmaY : y방향의 표준편차, 0 이면 sigmaX와 동일하게 설정됨


import sys, cv2, numpy as np 

src = cv2.imread("./images/rose.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("failed")
    sys.exit()

dst = cv2.GaussianBlur(src, (0,0), 1) # 블러효과를 더 주고 싶을때 2,3으로 설정
# 시그마가 1일때는 uint8에서 mean(7,7)과 같다
# 값이 커질수록 연산량 증가

dst2 = cv2.blur(src, (7,7)) 

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
