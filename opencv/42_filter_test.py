

################### 블러 + 엣지 효과 함수 만들어서 컬러영상에 사용하기 ##########################

import sys, cv2, numpy as np

cap = cv2.VideoCapture("./video/eagle.avi")

# 이 함수를 사용하면 속도가 너무 느림
# 사이즈를 줄이고 효과를 줌으로써 속도를 조금 올린다
# 이 함수는 카툰필터
def filter_1(img):
    # 사이즈 줄이기
    h, w = img.shape[:2]
    small_img = cv2.resize(img, (w//2, h//2))

    # 영상의 색상 단순화 작업
    blur = cv2.bilateralFilter(small_img, -1, 20, 8)
    # edge = cv2.Canny(img, 80, 100) # canny를 적용하면 그레이스케일로 변환됨
    edge = 255 - cv2.Canny(small_img, 80, 130) 
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # bgr로 변환시킴

    # 블러값에 엣지를 더하는 연산
    dst = cv2.bitwise_and(blur, edge) 

    # 사이즈 다시 키우고 보간법 옵션 주기
    dst = cv2.resize(dst, (w,h), interpolation=cv2.INTER_NEAREST) # 넣기 전보다 엣지 부분이 좀 더 선명해짐

    return dst

########### 그레이영상에 사용하기 ##################
# 이 함수는 스케치필터
def filter_2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 가우시안 필터 사용 , 표준편차 3
    blur = cv2.GaussianBlur(gray, (0,0), 3)

    # gray를 blur로 나눠주고 255 곱해줌, 스케치 필터 효과
    # 스케치 필터 카메라는 픽셀 값의 변화가 적은 평탄한 영역은 흰색으로 출력하고,
    # 에지 근방에서 어두운 영역을 검정색, 밝은 영역은 흰색으로 설정하면 구현할 수 있습니다.
    dst = cv2.divide(gray, blur, scale=255)

    return dst

if not cap.isOpened():
    print("video load failed")
    sys.exit()


fps = int(cap.get(cv2.CAP_PROP_FPS))
delay = round(1000 / fps)

mode = 0

while 1:
    
    ret, frame = cap.read()
  
    if not ret:
        break
    
    if mode == 1:
        frame = filter_1(frame)
        
    elif mode == 2:
        frame = filter_2(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        
    cv2.imshow('frame', frame)
    key = cv2.waitKey(20)

    if key == 27:
        break
    elif key == ord(' '):
        mode += 1
        if mode == 3:
            mode = 0


cap.release()
cv2.destroyAllWindows()
