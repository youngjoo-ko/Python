

################################# 두개의 동영상 전환하기 #######################################

import sys
import cv2
import numpy as np

# 두개의 동영상 불러오기
cap1 = cv2.VideoCapture("./video/video2.mp4")
cap2 = cv2.VideoCapture("./video/video1.mp4")

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed')
    sys.exit()


# 첫번째 동영상 뒷부분 2초, 두번째 동영상 앞부분 2초 합성
# 저장에 필요한 동영상 정보들 가져오기 
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT)) # 첫번째 동영상의 총 프레임 개수
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT)) # 두번째 동영상의 총 프레임 개수

fps = round(cap1.get(cv2.CAP_PROP_FPS)) # 초당 프레임 개수 24개

transition_frames = fps * 2  # 48개 , 영상이 3초 짜리라서 3 미만만 가능

print("frame_cnt1 :", frame_cnt1)
print("frame_cnt2 :", frame_cnt2)
print("fps:",fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
print('width:', w)
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')


# 출력 동영상 객체 생성(즉 편집해서 저장할 객체 만들기)
out = cv2.VideoWriter("./video/transition.avi", fourcc, fps, (w,h))

if not out.isOpened():
    print("open failed")
    cap.release() # 저장할 공간 마련해뒀던거 반납
    cap.exit()

# 첫번째 프레임
# while 1:
#     ret1, frame1 = cap1.read()
    
#     if not ret1:
#         break
    
#     out.write(frame1)

#     cv2.imshow('frame', frame1)
#     cv2.waitKey(10)


###########################################
# 1번 동영상 복사
for i in range(frame_cnt1 - transition_frames): # 마지막 2초부분만 삭제됨, 
    ret1, frame1 = cap1.read()

    if not ret1:
        break
    
    out.write(frame1) # 새로 만들어지는 영상의 frame1 부분에 저장(원숭이는 1초 정도)

    cv2.imshow('frame', frame1) # 1초짜리 영상 재생
    cv2.waitKey(15)

# 1,2번을 transition 효과 주고 합성하기 (이 코드 없이는 화면이 갑자기 전환된다)
for i in range(transition_frames): # 코끼리영상의 앞부분 프레임 48개(총 2초)
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    #####################################################################
    # w/transition_frames : 가로크기 / 48 (프레임 2초에 해당되는 가로크기?)
    dx = int(i *  w/transition_frames) # i는 프레임 1개, dx는 가로크기
    frame = np.zeros((h, w, 3), dtype=np.uint8) # 영상이 전환되는 부분을 넣을 프레임 새로 만들기
    frame[:, 0:dx, :] = frame2[:, 0:dx, :] # 새로운 영상 앞부분에 코끼리 영상의 앞부분 복사
    frame[:, dx:w, :] = frame1[:, dx:w, :] # 새로운 영상 뒷부분에 재생되면서 전환되는 원숭이 영상 복사
    #####################################################################


    ###################위 > 아래로 transition 합성하기 ####################
    # dx = int(i * h/transition_frames)
    # frame = np.zeros((h, w, 3), dtype=np.uint8)
    # frame[0:dx, :, :] = frame2[0:dx, :, :]
    # frame[dx:h, :, :] = frame1[dx:h, :, :]
    #########################################################################

    ###################대각선 transition 합성하기 ####################
    # dw = int(i * w/transition_frames) 
    # dh = int(i * h/transition_frames) 
   
    # frame = np.zeros((h, w, 3), dtype=np.uint8)
    # frame[dh:h, dw:w,  :] = frame1[dh:h, dw:w , :]
    # frame[0:dh, 0:dw,  :] = frame2[0:dh, 0:dw,  :]

    # dx = int(i * w/transition_frames) 
    # dy = int(i * h/transition_frames) 
    # d = w * h / 2
    # dz = dx * dy / 2

    # frame = np.zeros((h, w, 3), dtype=np.uint8)
    # frame[:, :, :] = frame1[:, :, :] # 1번 영상을 고정시켜놓고 
    # frame[0:dy, 0:dx, :] = frame2[0:dy, 0:dx, :] # 2번 영상만 대각선으로 내림
    #########################################################################

    # 가중치 구하는 함수 (디졸브 효과)
    # alpha = 1.0 - i / transition_frames # 알파는 투명도, 0~1사이의 값이 나오도록 설정
    # frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha, 0)
    
    out.write(frame)
    cv2.imshow("frame", frame)
    cv2.waitKey(15)

# 2번 동영상 저장
for i in range(transition_frames, frame_cnt2): # 코끼리 영상에서 잘린 앞부분을 제외하고서 부터 마지막까지!
    ret2, frame2 = cap2.read()
    
    if not ret2:
        break
    
    out.write(frame2)

    cv2.imshow('frame', frame2)
    cv2.waitKey(15)

