import sys
import random
import numpy as np
import cv2


src = cv2.imread('./images/contours2.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 오츠 전역이진화    
_, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 노이즈 제거
dst_no = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, (3,3), iterations=4)

# hier 키는 3차원 행렬
contours, hier = cv2.findContours(dst_no, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
h ,w = src.shape[:2]
dst = np.zeros((h,w,3), np.uint8)
print(hier)

# print(len(contours)) 

# dst2 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

########################## hierachy를 이용한 반복문##################################
# idx = 0 
# while idx >= 0:
    
#     c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
#     cv2.drawContours(dst, contours, idx, c, 1, cv2.LINE_8, hier) 

#     idx = hier[0, idx, 0]
##################################################################################

####################### N 개의 contours를 이용한 반복문 ##############################
for i in range(len(contours)): 
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 1, cv2.LINE_8) 
#####################################################################################


# print(hier) # next, prev, child, parent
# print(hier.shape) # (1,9,4)가 나오지만 1은 의미없는 숫자로 9x4행렬이 출력된것이나 마찬가지이다.


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
# cv2.imshow('dst_no', dst_no)
cv2.imshow('dst_no', dst_no)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows() 