########################  영상의 이진화 #################################
### threshold(임계값 함수)
## cv2.threshold(src, thresh, maxval, type, dst) -> retval , dst 리턴값이 2개
# src : 입력영상
# thresh : 사용자가 지정한 임계치
# maxval : 임계치 최대값(무조건 255)
# type : cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV 이 두가지 타입이 대부분 사용됨
# retval : 사용자가 지정한 임계치를 리턴하는 값
# dst : 출력영상

import sys, cv2, numpy as np

def on_th(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow("dst", dst)


src = cv2.imread("./images/cell_1.jpg", cv2.IMREAD_GRAYSCALE)

# retval 값(즉 200)을 첫번째로 받기때문에 영상출력이 되지 않음, dst로 받기위해 언더바 사용)
# _, dst = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)

if src is None:
    print("lmage load failed!")
    sys.exit()

cv2.imshow("src", src)
# cv2.imshow("dst", dst)
cv2.namedWindow("dst")
cv2.createTrackbar("threshold", "dst", 0, 255, on_th)
cv2.setTrackbarPos("threshold", "dst", 100)
cv2.waitKey()
cv2.destroyAllWindows()

