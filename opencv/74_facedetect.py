

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


src = cv2.imread('./images/son_heart.png')

if src is None:
    print('Image load failed!')
    sys.exit()

# 얼굴 검출 학습데이터 불러오기
# classifier = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
classifier = cv2.CascadeClassifier('./haarcascade_eye.xml')
# classifier.load(filename)

if classifier.empty():
    print('XML load failed!')
    sys.exit()

tm = cv2.TickMeter()
tm.start()

# 기본값은 1.1
# guys에서 얼굴 찾기
# faces = classifier.detectMultiScale(src, scaleFactor=1.2)
# 1.3을 주면 측면 얼굴은 못찾음

# son_black에서 눈 찾기
# faces = classifier.detectMultiScale(src, scaleFactor=1.2, minNeighbors=6) 

# son_heart에서 눈 찾기(왼쪽은 못찾고 입까지 찾아옴)
faces = classifier.detectMultiScale(src, scaleFactor=1.1, minNeighbors=4) 


for (x, y, w, h) in faces:
    cv2.rectangle(src, (x, y), (x+w, y+h), (255, 255, 0), 2)

tm.stop()
print(tm.getTimeMilli()) 
# 최소사이즈가 커지고 비율이 커질수록 속도가 빨라짐

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()