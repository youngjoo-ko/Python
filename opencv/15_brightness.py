
# 영상 화소 처리(point processing)
# 특정 좌표의 픽셀값을 변경하여 출력 영상의 해당 좌표 픽셀값으로 설정


## 밝기 조절 ##
# cv2.add(src1, src2, dst, mask, dtype)
# src1(입력) : 첫번째 영상 또는 스칼라
# src2(입력) : 두번째 영상 또는 스칼라
# dst(출력) : 밝게 편집한 결과영상(add연산 결과) 
# mask : 마스크 영상
# dtype : 출력영상 타입
# saturate (밝기조절수식) : dst(x,y) = saturate(src(x,y)+n)


import sys, cv2
import numpy as np


# img = cv2.imread("./images/woman.bmp", cv2.IMREAD_GRAYSCALE)


# if img is None:
#     print("failed")

# # dst = cv2.add(img, 100)
# dst = cv2.add(img, (100, 0, 0, 0)) # bgra 위 코드는 이런식으로 들어간것
# # dst = img + 100 # img가 numpy 이기 때문에 100을 더해도 될까? 안됨. 
# # 왜 ? 예를들면 (180, 256, 350, 290) 이런식의 연산이 되고, 256부터는 1로 다시 시작하기 때문에 검은색이 섞여보이는것

# cv2.imshow("img", img)
# cv2.imshow("dst", dst)
# cv2.waitKey()

########## 컬러영상 ###############
img = cv2.imread("./images/woman.bmp")


if img is None:
    print("failed")

# dst = cv2.add(img, 100) # 푸른톤이 더 선명해짐 그 이유는 (100, 0, 0, 0) 만큼 더해졌기 때문
dst = cv2.add(img, (100,100,100,0)) # 전체적으로 밝아짐
dst2 = np.clip(img + 100., 0, 255).astype(np.uint8)

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)

cv2.waitKey()