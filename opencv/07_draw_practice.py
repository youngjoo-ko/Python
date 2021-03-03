import numpy as np
import cv2
import sys

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("EVENT_LBUTTONDOWN:{},{}".format(x,y))


img = np.full((800, 800, 3), 255, dtype=np.uint8)

# 라이언 그리기(BGR)
cv2.circle(img, (400,400), 150, (0,51,102), 2, cv2.LINE_AA) 
cv2.ellipse(img, (320,275), (30,35), -30, 180, 360, (0,51,102), 2, cv2.LINE_AA) 
cv2.ellipse(img, (480,275), (30,35), 30, 180, 360, (0,51,102), 2, cv2.LINE_AA) 
# 눈썹
cv2.line(img, (304,335) , (360,3 35), (0,0,0), 5, cv2.LINE_AA)
cv2.line(img, (430,335) , (486,335), (0,0,0), 5, cv2.LINE_AA)
# 눈
cv2.circle(img, (338,371), 6, (0,0,0), -1, cv2.LINE_AA)
cv2.circle(img, (459,371), 6, (0,0,0), -1, cv2.LINE_AA)


cv2.namedWindow("img")
cv2.imshow("img", img)
cv2.setMouseCallback("img", on_mouse)

cv2.waitKey()
cv2.destroyAllWindows()

