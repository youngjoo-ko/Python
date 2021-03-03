

###################### gaussian filtering  ##############################
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

cv2.imshow("src", src)

for sigma in range(1,6):
    dst = cv2.GaussianBlur(src, (0,0), sigma)
    desc = 'sigma : {}'.format(sigma)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA )

    cv2.imshow("dst", dst)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()
