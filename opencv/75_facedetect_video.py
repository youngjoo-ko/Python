

############### 캐스케이드 분류기 함수 ######################

## cv2.CasccadeClassifier.detectMultiScale(image, scaleFactor=None, minNeighbors=None, 
# flags=None, minSize=None, maxSize=None) > result
'''
• image: 입력 영상 (cv2.CV_8U)
• scaleFactor: 영상 축소 비율. 기본값은 1.1이며 1.1배로 점점 키워가면서 검출한다(크면 속도가 빠름, 세밀도는 떨어짐)
• minNeighbors: 얼마나 많은 이웃 사각형이 검출되어야 최종 검출 영역으로 설정할지를 지정(사각형의 개수). 기본값은 3.
• flags: (현재) 사용되지 않음
• minSize: 최소 객체 크기. (w, h) 튜플. (24,24) 부터 시작
- minSize를 지정해서 속도를 더 빠르게 할 수 있다
• maxSize: 최대 객체 크기. (w, h) 튜플. (24,24) 부터 시작
• result: 검출된 객체의 사각형 정보(x, y, w, h)를 담은 numpy.ndarray. shape=(N, 4). dtype=numpy.int32.

'''

import sys
import numpy as np
import cv2


cap = cv2.VideoCapture('./video/face.mp4')

if not cap.isOpened:
    print("Video open failed")
    sys.exit()


### 프레임 정보 확인
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h =  round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(w,h)

### ######## 비디오 출력(저장)하기
# VideoWriter(filename, fourcc, fps, framesize, isColor(기본값 true))
# : 해당 정보와, 수행결과(true, false)를 리턴해준다
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('./video/face_detect_video.avi', fourcc, fps, (w, h))


# 얼굴 검출 학습데이터 불러오기
face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
eye_classifier = cv2.CascadeClassifier('./haarcascade_eye.xml')
# classifier.load(filename)

if face_classifier.empty() or eye_classifier.empty():
    print('XML load failed!')
    sys.exit()


tm = cv2.TickMeter()
tm.start()

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)

delay = int(1000/fps)

while 1:
    ret, frame = cap.read()

    if not ret:
        break

    faces = face_classifier.detectMultiScale(frame, minSize=(1000,1000)) 

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3, cv2.LINE_AA)
        
        eyes = eye_classifier.detectMultiScale(frame, minSize=(200,200), maxSize=(350,350), scaleFactor=1.2, minNeighbors=15)

        for (x2, y2, w2, h2) in eyes:
            cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 3, cv2.LINE_AA)

    out.write(frame)
    cv2.imshow("frame", frame)

    if cv2.waitKey(delay) == 27:
        break


cap.release()
cv2.destroyAllWindows()