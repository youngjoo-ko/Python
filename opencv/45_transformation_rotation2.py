

########################### 로테이션(각도) 자동 변환 #######################
### 영상 회전 변환행렬(2x3) 구하는 함수
## cv2.getRotationMatrix2D(center, angle, scale)
# center : 회전 중심 좌표
# angle : 회전각도(degree), 음수는 시계 방향
# scale : 확대 비율

import sys, cv2, numpy as np

src = cv2.imread("./images/sea.png")

if src is None:
    print("failed")
    sys.exit()

# 중심점 구하기
center_pt = (src.shape[1] / 2, src.shape[0] / 2) # 가로 세로 반반해서 중심점 구함

# 회전 변환행렬 구하기
rotation_arr = cv2.getRotationMatrix2D(center_pt, 45, 1)

# 어파인함수에 적용
dst = cv2.warpAffine(src, rotation_arr, (0,0), borderValue = (255,255,255))
# 이미지 가운데 중심점을 기준으로 반시계 방향으로 45도 돌아감

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()