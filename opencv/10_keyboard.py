
import sys
import cv2
import numpy as np


######### 키보드 이벤트 ##########
# cv2.waitKey(delay)
# delay : 밀리초단위 대기시간, delay <=0 무한정 대기, default = 0
# retVal(눌린키값) : 눌린키의 아스키코드를 반환, 눌리지 않으면 -1
# 참고 : waitKey() 함수는 OpenCV 창이 하나라도 있을 때 동작함
# 특정 키 입력을 확인하려면 ord() 함수를 이용
# 주요 키 : esc(27), enter(13), tap(9)

img = cv2.imread("./nacho.png", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("image load failed")
    sys.exit()

cv2.namedWindow("image")
cv2.imshow("image", img)



# esc 키 눌렀을 때 종료하는 이벤트
# while 1:
#     if cv2.waitKey() == 27:
#         break

# i, I를 눌렀을 때 색반전한 이미지가 나오는 이벤트, esc를 눌렀을때 종료
while 1:
    keycode = cv2.waitKey()
    if keycode == ord('I') or keycode == ord('i'):
        inversed = ~img
        cv2.imshow("image", inversed)
        
    elif keycode == 27:
        break

cv2.destroyAllWindows()