

################### 블러 + 엣지 효과 함수 만들어서 컬러영상에 사용하기 ##########################

import sys, cv2, numpy as np

# 이 함수를 사용하면 속도가 너무 느림
# 사이즈를 줄이고 효과를 줌으로써 속도를 조금 올린다

def filter_1(img):
    # 사이즈 줄이기
    h, w = img.shape[:2]
    small_img = cv2.resize(img, (h//2, w//2))

    blur = cv2.bilateralFilter(small_img, -1, 15, 8)
    # edge = cv2.Canny(img, 80, 100) # canny를 적용하면 그레이스케일로 바뀜
    edge = 255 - cv2.Canny(small_img, 80, 150) 
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # bgr로 변환

    dst = cv2.bitwise_and(blur, edge) # 블러값에 엣지를 더하는 연산

    # 사이즈 다시 키우고 보간법 옵션 주기
    dst = cv2.resize(dst, (w,h), interpolation=cv2.INTER_NEAREST) # 넣기 전보다 엣지 부분이 좀 더 선명해짐

    return dst

########### 그레이영상에 사용하기 ##################

def filter_2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 가우시안 필터 사용 , 표준편차 3
    blur = cv2.GaussianBlur(gray, (0,0), 3)

    # gray를 blur로 나눠주고 255 곱해줌, 스케치 필터 효과
    # 스케치 필터 카메라는 픽셀 값의 변화가 적은 평탄한 영역은 흰색으로 출력하고,
    # 에지 근방에서 어두운 영역을 검정색, 밝은 영역은 흰색으로 설정하면 구현할 수 있습니다.
    dst = cv2.divide(gray, blur, scale=255)

    return dst


cap = cv2.VideoCapture("./video/nacho_in_beach.mp4")

if not cap.isOpened():
    print("video load failed")
    sys.exit()

### 프레임 정보 확인
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h =  round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)
print(fourcc)

out1 = cv2.VideoWriter('./video/nacho_filter_test1.avi', fourcc, fps, (w,h))
out2 = cv2.VideoWriter('./video/nacho_filter_test2.avi', fourcc, fps, (w,h))

if not out1.isOpened() or not out2.isOpened():
    print("video out failed")
    sys.exit()

while 1:
    ret, frame = cap.read()

    if not ret:
        break

    frame1 = filter_1(frame)
    frame2 = filter_2(frame) # 그레이 스케일이기 때문에 저장이 안됨, 따라서 컨버트 해줘야함
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_GRAY2BGR)

    out1.write(frame1)
    out2.write(frame2)

    cv2.imshow("frame1", frame1)
    cv2.imshow("frame2", frame2)

    # 지금 while문에서 frame이 돌아가고 있으므로 영상이 재생되는 동안에 끄면, 그 만큼만 저장됨

    if cv2.waitKey(5) == 27:
        break

cap.release()
cv2.destroyAllWindows()
