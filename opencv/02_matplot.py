# pip install matplotlib 설치

import matplotlib.pyplot as plt 
import cv2

# 컬러영상 출력
# opencv는 RGB를 BGR 순서로 읽는다
imgBGR = cv2.imread("./nacho.png")

# 그래서 CONVERTING 해준다 
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis("off") # axis 축을 없앰
# plt.imshow(imgRGB)
plt.imshow(imgBGR)
plt.show()

# 흑백(그레이스케일)으로 출력
imgGray = cv2.imread("./nacho.png", cv2.IMREAD_GRAYSCALE)
plt.imshow(imgGray, cmap="gray") # cmap(color map을 gray로 설정)
plt.show()

# subplot을 이용한 영상 출력
plt.subplot(221), plt.axis("off"), plt.imshow(imgRGB)
plt.subplot(222), plt.axis("off"), plt.imshow(imgGray, cmap="gray")
plt.subplot(223), plt.axis("off"), plt.imshow(imgBGR)

plt.show()