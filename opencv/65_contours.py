import sys
import random
import numpy as np
import cv2


src = cv2.imread('./images/contours.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# hier 키는 3차원 행렬
contours, hier = cv2.findContours(src, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(len(contours)) # 객체는 9개

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

idx = 0 
while idx >= 0:
    
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_8, hier) 

    idx = hier[0, idx, 0]
print(hier) # next, prev, child, parent
print(hier.shape) # (1,9,4)가 나오지만 1은 의미없는 숫자로 9x4행렬이 출력된것이나 마찬가지이다.


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows() 