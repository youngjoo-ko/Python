

import sys, cv2, numpy as np

src = cv2.imread("./images/woman.bmp", cv2.IMREAD_GRAYSCALE)


if src is None:
    print("failed")
    sys.exit()

## 양방향 필터링 함수
# cv2.bilateralFilter(src, d, simgaColor, sigmaSpace, dst, borferType )
# src : 입력영상
# d : 필터링에 사용될 아웃픽셀의 거리(지름), -1을 설정하고 쭉 쓰는 것이 좋다
# sigmarColor: 색공강에서의 필터 표준편차
# sugmaSpace : 좌표공간의 필터 표준편차

dst = cv2.bilateralFilter(src, -1, 10, 5) 
# 시그마가 커지면 블링 효과가 더 커진다
# 시그마스페이스 값이 5보다 커지면 가우시안필터 사이즈가 커지므로 연산속도가 느려짐

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
