

################################## 영상의 확대, 축소 #################################

import sys, cv2, numpy as np

src = cv2.imread("./images/rose2.bmp") 
print(src.shape)

if src is None:
    print("failed")
    sys.exit()

## cv2.resize(src, dsize, dst, fx, fy, inerpolation(보간법))
# src : 입력영상
# dsize: 결과영상의 크기 (w,h) 튜플로 표현, (0,0)이면 fx,fy값을 통해 결정됨
# fx, fy : x, y 방향의 스케일 비율 (몇배로 확대, 축소할건지)

dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920,1280)) # INTER_LINEAR 기본값
dst3 = cv2.resize(src, (1920,1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920,1280), interpolation=cv2.INTER_LANCZOS4)


cv2.imshow("src", src)
cv2.imshow("dst1", dst1[500:800, 400:800])
cv2.imshow("dst2", dst2[500:800, 400:800])
cv2.imshow("dst3", dst3[500:800, 400:800])
cv2.imshow("dst4", dst4[500:800, 400:800])
cv2.waitKey()

cv2.destroyAllWindows()
