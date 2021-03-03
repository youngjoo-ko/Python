
import sys
import cv2

################ 비디오 출력(녹화 & 저장) #################
cap = cv2.VideoCapture('./video/video2.mp4')

if not cap.isOpened:
    print("Video open failed")
    sys.exit()

### 프레임 정보 확인
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h =  round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

### ######## 비디오 출력(저장)하기
# VideoWriter(filename, fourcc, fps, framesize, isColor(기본값 true))
# : 해당 정보와, 수행결과(true, false)를 리턴해준다
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
print(fourcc)

out = cv2.VideoWriter('./video/out_video.avi', fourcc, fps, (w,h))
# edge = cv2.VideoWriter('./video/out_video_edge.avi', fourcc, fps, (w,h))

if not out.isOpened():
    print("open failed")
    cap.release() # 저장할 공간 마련해뒀던거 반납
    cap.exit()

delay = int(1000/fps)

while 1:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame
    edge = cv2.Canny(frame, 50, 150) # 리턴값은 그레이스케일이라 영상 재상 안됨?
    edge_2 = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    #out.write(inversed)
    out.write(edge_2)

    cv2.imshow("frame", frame)
    cv2.imshow("inversed", inversed)
    cv2.imshow("edge2", edge_2)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()
