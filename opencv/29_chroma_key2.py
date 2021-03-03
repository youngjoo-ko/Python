

############################# 그린 스크린 영상에 원숭이 배경 합성하기 #################



import sys, cv2, numpy as np

cap1 = cv2.VideoCapture("./video/chromakey/chromakey_green.mp4")
cap2 = cv2.VideoCapture("./video/chromakey/monkey1.avi") # 두개의 영상은 사이즈가 다르다

if not cap1.isOpened():
    print("video open failed")
    sys.exit()

if not cap2.isOpened():
    print("video open failed")
    sys.exit()

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) # 프레임 사이의 간격

# 합성 플래그
composit_flag = False

while 1:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    if composit_flag: # composit_flag 가 트루면
        ret2, frame2 = cap2.read()

        if not ret2:
            break
        
        frame2 = cv2.resize(frame2, (w,h)) # frame1의 사이즈로 frame2를 리사이즈 해준다
        
        # hsv로 변환하여 블루스크린 동영상의 파란색만 추출하기(100~125, 150~255, 255)
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (45, 200, 0), (70, 255, 255))
        cv2.copyTo(frame2, mask, frame1) # frame1의 파란색배경이 제외되고(mask 만큼) 그 부분에 frame2가 적용됨

    cv2.imshow("frame", frame1)
    key = cv2.waitKey(delay)

    # space bar를 이용해서 플래그 toggle(on/off) 시키기 
    if key == ord(' '):
        composit_flag = not composit_flag
    elif key == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()