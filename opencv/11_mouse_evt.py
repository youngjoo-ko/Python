
import sys
import cv2
import numpy as np

## 마우스 이벤트
## GUI 이벤트는 운영체제(윈도우)가 백그라운드에서 실행하고 있다
## setMouseCallback 함수를 통해 onMouse로 다시 갖고오는 것 이후로 이벤트는 opencv가 처리한다

# setMouseCallback(windowName, onMouse, param)
# windowName : 마우스 이벤트를 수행할 창 이름
# onMouse : 마우스 이벤트 처리를 위한 콜백(자동으로 호출)함수 이름, 핸들링 함수
# param : 콜백함수에 전달할 데이터

# onMouse(event, x, y, flags, param)
# : 4개의 변수를 받아 이벤트를 만든다
# event : 이벤트 종류 cv2.__EVENT_ 로 시작하는 상수
# x, y : 이벤트 발생 좌표
# flags : 마우스 이벤트 발생 시 상태 cv2.EVENT_FLAG_로 시작하는 상수(& 연산자로 새로운 조건을 달 수 있다)
# param : setMouseCallback


## flags
# cv2.EVENT_FLAG_LBUTTON : 1 (마우스 왼쪽 버튼을 눌렀을때) 0 0 | 0 0 0 1
# cv2.EVENT_FLAG_RBUTTON : 2 (마우스 오른쪽 버튼을 눌렀을 때) 0 0 | 0 0 1 0
# cv2.EVENT_FLAG_MBUTTON : 4 (마우스 가운데 버튼을 눌렀을 때) 0 0 | 0 1 0 0
# cv2.EVENT_FLAG_CTRLKEY : 8 (컨트롤 키를 눌렀을 때) 0 0 | 1 0 0 0
# cv2.EVENT_FLAG_SHIFTBUTTON : 16 (SHIFT키를 눌렀을 때) 0 1 | 0 0 0 0
# cv2.EVENT_FLAG_ALTBUTTON : 32 (ALT 버튼을 눌렀을 때) 1 0 | 0 0 0 0

# 마우스 왼쪽 버튼을 눌렀을때 해당 좌표값 출력하는 이벤트 만들기
# oldx = oldy = -1  # 글로벌변수로 선언하지 않으면 이렇게 초기화해줘야 함

def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y  # 이전 x,y 좌표는 마우스를 클릭할때 생성되므로 여기서 변수를 선언한다
        print("EVENT_LBUTTONDOWN:{},{}".format(x,y))

    # 마우스 왼쪽버튼을 눌렀다 뗐을때 좌표값 출력하는 이벤트
    elif event == cv2.EVENT_LBUTTONUP:
        print("EVENT_LBUTTONUP:{},{}".format(x,y))

    
    elif event == cv2.EVENT_MOUSEMOVE:
        #if flags == cv2.EVENT_FLAG_LBUTTON: # 마우스 왼쪽 버튼을 누른상태에서 이동했을 때만 좌표값을 찍음(+다른키 누르면 찍지 않음)
        if flags & cv2.EVENT_FLAG_LBUTTON: # 마우스 왼쪽버튼을 누르고 다른키를 눌러도 마우스를 이동하면 좌표값 찍음 비트연산자를 참고
            # print('EVENT_MOUSEMOVE: {}, {}'.format(x,y))
            # 마우스를 누를 상태에서 원 그리기
            # cv2.circle(img, (x,y), 5 , (0,0,255), -1) # 아주 작은 동그란 점이기 때문에 빨리 그었을때 점선처럼 그려진다
            # line함수는 시작점, 끝점이 있기때문에 이전 x,y 좌표를 저장해놓을 필요가 있다
            cv2.line(img, (oldx, oldy), (x,y), (0,0,255), 2, cv2.LINE_AA)
            cv2.imshow("image", img)
            oldx, oldy = x, y # 이전 x, y 좌표를 다시 시작점에 넣어줌 

# 255를 곱하기 전에는 검은색 
img = np.ones((480,640,3), dtype=np.uint8)  * 255 # 흰색

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)

cv2.imshow("image", img)
cv2.waitKey() # 아무키든 누르면 종료
cv2.destroyAllWindows()