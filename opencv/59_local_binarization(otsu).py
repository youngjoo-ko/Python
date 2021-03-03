

import sys, cv2, numpy as np


src = cv2.imread("./images/sudoku.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("lmage load failed!")
    sys.exit()

# 오츠를 사용한 전역 이진화
_, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 이진화
dst2 = np.zeros(src.shape, np.uint8)

# 입력 영상을 가로, 세로로 4등분(총 16등분)
bw = src.shape[1] // 4 # 분할한 사각형의 가로 사이즈
bh = src.shape[0] // 4 # 분할한 사각형의 세로 사이즈

for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw]

        # dst_를 파라미터로 사용하면 입력 및 출력으로 사용할 수 있다
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)


cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

