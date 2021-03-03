
################ 비디오 입력(프레임 캡쳐 & 화면표시 & 재생)#################
# 프레임 
# 24프레임 / 초  : 1초당 재생되는 정지화면이 24개
# 코덱 : 인코딩 된 것을 디코딩하는 프로그램

### fourcc(four character code) : 4개의 문자 코드
# 정의 : 동영상 파일의 코덱, 압축방식, 색상, 픽셀 등을 정의하는 정수 값
# 종류 
# *'DIVX' : DIVX MPEG-4 코덱 , 일반적으로 사용
# *'XVID' : XVID MPEG-4 코덱
# *'FMP4' : FFMPEG MPEG-4 코덱
# *'X264' : H.264/AVC 코덱
# *'MJPG' : Motion-JPEG-4 코덱

import sys
import cv2

# 비디오 파일 열기
# cv2.VideoCapture 클래스 사용 : 카메라 캡쳐와 동영상을 불러올 수 있음

cap = cv2.VideoCapture('./video/video2.mp4')

if not cap.isOpened:
    print("Video open failed")
    sys.exit()

# 불러온 비디오의 프레임 크기, 전체 프레임수, FPS(초당 프레임수) 확인
print('frame width:', cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # get은 리턴값이 실수형(float)이다
print('frame height:', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT))) # int로 형변환 가능

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

# 비디오의 각 프레임 처리
while 1:
    ret, frame = cap.read() # 프레임과 리턴값을 받아온다(해당 프레임과 false/true)
    
    if not ret:
        break
    
    # inversed = ~frame # 색 반전
    edge = cv2.Canny(frame, 50, 150) # 윤곽선만 

    cv2.imshow('frame', frame) # 총 85개의 프레임이 재생된 것
    cv2.imshow('edge', edge) 
    # cv2.imshow('inversed', inversed)

    # 임계치

    # 각 프레임당 딜레이 시간 0.02초, esc를 누를때까지
    if cv2.waitKey(20) == 27: 
        break
    
cap.release() # 비디오 닫기
cv2.destroyAllWindows()