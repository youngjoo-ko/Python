import numpy as np
import cv2

########################### 영상에 도형, 선 그리기 #############################
# 1. 직선 그리기
# cv2.line(img, pt1, pt2, color, thickness, lineType, shift)
# img : 도화지 개념
# pt1, pt2 : 선의 시작과 끝점(튜플로 표현)
# color : 선의 색상
# thickness : 선의 두께 (기본값은 1)
# lineType : 선타입(cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA) ,
# - 기본값은 cv2.LINE_8, 하지만 AA(antialiasing)를 가장 많이 씀
# shift : 좌표값의 축소 비율, 기본값은 0
# alias란 ? 픽셀을 확대했을 때 계단처럼 보이는 현상
# antialiasing 이란? 계단처럼 보이는 부분 주변에 비슷한색상을 칠해서 부드럽게 보이게 하는 방법


# 도화지는 그레이스케일이면 컬러선을 그릴 수 없다
# 흰색 바탕인 800 * 800 도화지 만들기
img = np.full((800, 800, 3), 255, dtype=np.uint8)

# 수평으로 파란 직선 그리기
# cv2.line(img, (100,100), (400,100), (255,0,0), 5)

# 대각선으로 빨간색 직선 그리기
# cv2.line(img, (100,100), (200,400), (0,0,255), 5)

# 2. 사각형 그리기(2가지 방법)
# cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# cv2.rectangle(img, rec, color, thickness, lineType, shift)

# cv2.rectangle(img, (70,220) , (180,280) , (0, 128, 0), -1) 
# 70, 220 : 왼쪽 상단 모서리 좌표값
# 180 , 280 : 오른쪽 하단의 모서리 좌표값
# -1 : 배경을 채우는 것


# cv2.rectangle(img, (50,200,150,150) , (0, 255, 0), 5) 
# 50 , 200 : x, y 좌표값(사각형의 왼쪽상단 모서리의 좌표)
# 150 : x,y 좌표값에서부터 x축으로 뻗은 직선(오른쪽 상단의 모서리)의 너비(사각형의 넓이)
# 150 : 오른쪽 상단의 모서리로 부터 y쪽으로 뻗은 직선 (사각형의 높이)

# 3. 원 그리기
# cv2.circle(img, center, radius, color, thickness, lineType, shift) 
# center : 중심점(튜플로 x,y 좌표값)
# radius : 반지름
# cv2.circle(img, (300,300), 100, (255,255,0), -1, cv2.LINE_AA) 

# 4. 타원 그리기
# cv2.ellipse(img, center, size(가로세로), 앵글, 시작각도, 끝각도, color, thickness, lineType, shift)
# cv2.ellipse(img, (400,500), (200,150), 0, 0, 360, (0,0,255), -1, cv2.LINE_AA)
cv2.ellipse(img, (400,500), (200,150), 90, 0, 360, (0,0,255), 3, cv2.LINE_AA) # 세로로 선 타원
cv2.ellipse(img, (400,500), (200,150), 45, 0, 360, (255,0,0), 3, cv2.LINE_AA) # 45도 각도로 선 타원
cv2.ellipse(img, (400,500), (200,150), 0, 90, 360, (0,255,0), -1, cv2.LINE_AA) # 시작각도로부터 시계방향으로 돔
cv2.ellipse(img, (400,500), (200,150), 0, 180, 360, (0,0,255), -1, cv2.LINE_AA) # 반타원
#cv2.ellipse(img, (400,500), (200,150), 0, 0, 180, (0,0,255), -1, cv2.LINE_AA) # 원 x
# 마지막에 그린 도형이 맨위로 올라온다

# 7. 다각형 그리기
# cv2.polylines(img, pts, isClose, color, thickness, lineType, shift)
pts = np.array([[300, 200], [300, 150], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255,255,0), 3)


# 6. 문자열 출력
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, shift)
# org : 문자열의 시작점(x,y)
# fontFace : 폰트타입
# fontScale : 폰트 사이즈
# thickness : 폰트 두께
text = "My Picture"
cv2.putText(img, text, (200, 600), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 2, cv2.LINE_AA)


cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

