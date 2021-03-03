
import sys, cv2, numpy as np

def drawROI(img, corners):
    cpy = img.copy() # 전송받은 이미지의 복사본 만들기
    c1 = (192, 192, 255) # 원 컬러 설정
    c2 = (128, 128, 255) # 직선 컬러 설정

    for pt in corners: # 여기서 corners는 크기조절 사각형 좌표값
        # c1 컬러로 원을 그린다
        # 3. 원 그리기
        # cv2.circle(img, center, radius, color, thickness, lineType, shift) 
        # center : 중심점(튜플로 x,y 좌표값)
        # radius : 반지름
        # cv2.circle(img, (300,300), 100, (255,255,0), -1, cv2.LINE_AA) 
       
        # 중심점에 튜플이 필요하기 때문에 리스트 -> 튜플 로 변환해준다
        cv2.circle(cpy, tuple(pt), 25, c1, -1, cv2.LINE_AA)

    # 각 코너는 튜플로 변환
    # 각 모서리를 잇는 직선 그리기
    cv2.line(cpy, tuple(corners[0]), tuple(corners[1]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1]), tuple(corners[2]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2]), tuple(corners[3]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3]), tuple(corners[0]), c2, 2, cv2.LINE_AA)

    # 가중치 합성
    # 원본 img 가중치를 0.7로 , 크기조절 사각형이 그려진 cpy 가중치를 0.3으로 둘이 합침
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)

    return disp

def on_mouse(event, x, y, flags, param):
    global src_coord, drag_src, pt_old, src_coord # 여기서 global 설정 유의할것!
    
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            # cv2.norm() 은 두 좌표간의 유클리디안 거리값을 측정하는 함수
            if cv2.norm(src_coord[i] - (x, y)) < 25: # 25는 어떻게 나온거지? 원의 반지름
                # 모서리 (src_coord[i]) 로부터 25이하로 떨어져 있는 곳을 클릭했을 때 움직이겠다는 뜻
                # 즉, 원을 벗어난 곳을 클릭하면 움직일 수 없음 
                drag_src[i] = True # 눌러졌는지 상태값을 저장하기 위함
                pt_old = (x,y)
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            drag_src[i] = False # 마우스를 뗐을 때 무브이벤트가 발생하지 않도록 False로 저장

    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if drag_src[i]: # 왼쪽버튼이 눌렸을 때(True)를 조건으로 줌 
                dx = x - pt_old[0] # pt_old는 lbuttondown 이벤트에서 가져온 x,y 
                dy = y - pt_old[1] # dx, dy 는 내가 직접 설정한 선택영역의 좌표 
                # 즉 이 두값을 빼면 내가 선택한 좌표에서 처음 왼쪽버튼을 눌렀을때 생성된 좌표를 빼게 되고
                # 그럼 그 중간의 공간이 남게 된다

                src_coord[i] += (dx, dy)
                # 끌고가는 모서리의 좌표값을 계속해서 더해줌 
                # 각 모서리 좌표에서 중간에 남은 공간을 더하면 x,y 좌표가 이동하면서
                # 최종적으로 내가 선택한 영역의 위치에 서게됨


                # 좌표가 이동되는 모습을 자연스럽게 이미지로 출력해줌
                # 최종적으로 새로운 모서리 4개(선택영역)을 원본이미지에 그림
                cpy = drawROI(src, src_coord) 

                # 모서리를 이동한 모양을 보여줌
                cv2.imshow("img", cpy)
                pt_old = (x, y) # 다시 변수로 초기화를 해줘야 다른 모서리의 좌표가 들어갈 수 있음
                break

############################################################################################


src = cv2. imread("./images/test.jpg")

if src is None:
    print("image open failed")
    sys.exit()

h, w = src.shape[:2] # 원본의 높이, 너비 가져옴
dw = 500 # 이건 왜 500?

# A4 용지 크기 : 210 * 297cm, 세로크기 설정
dh = round(dw * 297 / 210)

# 크기 조절 사각형 영역 설정
src_coord = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)

# 출력 영상 좌표(반시계 방향)
dst_coord = np.array([[0,0], [0, dh-1], [dw-1, dh-1], [dw-1, 0]], np.float32)
drag_src = [False, False, False, False] # ??

# 모서리점, 사각형 그리기
disp = drawROI(src, src_coord) # 원본 이미지에 크기조절 사각형 그리기 

cv2.imshow("img", disp) # 보여주기
cv2.setMouseCallback("img", on_mouse) # 만든 함수 적용

while 1:
    key = cv2.waitKey()
    if key == 13: # 엔터를 누르면 선택영역을 추출
        break
    elif key == 27:
        cv2.destroyAllWindows("img")
        sys.exit()


# 투시변환
# pers : 크기조절 사각형의 원래 좌표점과 내가 선택한 영역의 좌표점, 변환행렬 생성
pers = cv2.getPerspectiveTransform(src_coord, dst_coord) 

# cv2.warpPerspective(src, M, dsize, dst, flag, borderMode, borderValue) 
# • src: 입력 영상
# • M: 3x3 투시 변환 행렬. 실수형.
# • dsize: 결과 영상 크기. (w, h) 튜플. (0, 0)이면 src와 같은 크기로 설정
# • dst: 출력 영상
# • flags: 보간법. 기본값은 cv2.INTER_LINEAR
# • borderMode: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT
# • borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.

dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

# 결과 영상 출력
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()