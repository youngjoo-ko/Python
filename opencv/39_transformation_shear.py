

################################## 영상의 이동 #################################

import sys, cv2, numpy as np

src = cv2.imread("./images/sea.png")


if src is None:
    print("failed")
    sys.exit()

# 어파인 변환 행렬 생성(어파인 변환행렬은 2x3인 단위행렬)
aff = np.array([[1,0.5,0], # x축 밀림(?)
               [0,1,0]], dtype=np.float32) 


# 이동(변환행렬을 변환함수에 대입)
dst = cv2.warpAffine(src, aff, (0,0))

# 이동하면서 잘린 이미지까지 출력하기
h, w = src.shape[:2]
dst2 = cv2.warpAffine(src, aff, (w + int(h*0.5), h))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()

cv2.destroyAllWindows()
