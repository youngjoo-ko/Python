
import numpy as np
import cv2

# 트랙바(trackbar)
# : 프로그램 동작 중 사용자가 지정한 범위 안의 값을 선택할 수 있는 컨트롤 입니다.

# cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
# trackbarName : 트랙바 이름
# windowName : 트랙바를 생성할 창 이름
# value : 트랙바의 위치 초기값
# count : 최대값, 최솟값은 항상 0
## onChange: 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름
# onChange(position) : 위치값을 변수로 받음

def on_level_change(pos):
    level = pos * 16 # 256
    # 레벨 16으로 가면 다시 검은색이 되는 이유는 255를 넘었기 때문 그래서 다음 if문으로 처리
    # if level >= 256:
    #     level = 255

    # 더쉽게 하는 np함수
    level = np.clip(level, 0, 255) # 0보다 작은값은 0, 255보다 큰값은 255
    img[:, :] = level # 행렬을 그 색깔로 채운다

    cv2.imshow("image", img)
    print(level)

img = np.zeros((480, 640), np.uint8)

cv2.imshow("image", img)
# 트랙바는 이미지 창(namedwindow, imshow)을 생성한 이후에 사용해야 한다
cv2.createTrackbar("level_bar", "image", 0, 16, on_level_change)
cv2.waitKey()
cv2.destroyAllWindows()