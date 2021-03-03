
import sys, cv2, numpy as np

## Canny edge 검출함수
# cv2.Canny(image, threshold1, threshold2, edge = None, apertusize=None, L2 gradient)
# image : 입력영상
# threshold1 : 하단 임계값(최소)
# threshold2 : 싱딘 임계값(최대) 정해진비율은 없다, 비율(1:2또는 1:3, 지정하지만 않으면 1:2)
# apertusize : 소벨연산용 커널(기본값 3)
# LRgradient : True이면 L2 morm, False 이면 L1 norm을 이용 ,기본값은 False 이다.
# L2는 거리계산, L1은 거리의 절대값


src = cv2.imread("./images/canny1.png", cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread("./images/canny2.jpg", cv2.IMREAD_GRAYSCALE)
src3 = cv2.imread("./images/woman.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("image load failed")
    sys.exit()

dst = cv2.Canny(src, 50, 150)
dst2 = cv2.Canny(src2, 150, 200)
dst3 = cv2.Canny(src3, 150, 200)


cv2.imshow("src", src)
cv2.imshow("src2", src2)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()
