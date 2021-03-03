

########################### 로테이션(각도) 수동 변환 #######################
## 중심각도는 원점(0,0)
import sys, cv2, math, numpy as np

src = cv2.imread("./images/sea.png")

if src is None:
    print("failed")
    sys.exit()

# degree를 radian 단위로 수정
rad = -45 * math.pi / 180   # degree 각도 45도를 redian으로, 즉 반시계 방향으로 회전
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()