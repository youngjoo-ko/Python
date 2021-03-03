

#################### 미디안 필터(노이즈 제거) 사용하기 ##############
## cv2.medianBlur(src, ksize, dst)



import sys, cv2, numpy as np

noise = cv2.imread("./images/noise.bmp", cv2.IMREAD_GRAYSCALE)
dst = cv2.medianBlur(noise, 5) # 커널사이즈를 크게 잡으면 이미지가 뭉치는 현상이 발생

print(noise.shape)
cv2.imshow("noise", noise)
cv2.imshow("dst", dst)
cv2.waitKey()