

import sys, cv2, numpy as np


src = cv2.imread("./images/rice.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("lmage load failed!")
    sys.exit()

# 오츠타입은 사용자지정 임계치를 대표값 0으로 준다 (다른값으로 지정해도 오츠연산이 자동계산해준다)
# th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU) # or연산 생략 가능
th, dst2 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) 
# 이전 파일처럼 오류가 안나는 이유는 임계치를 자동으로 넘기는 대표값을 줬기 때문인 것 같다

print("오츠의 임계치 : ", th)

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()

