

########################### 트랙바를 이용한 특정 영역의 컬러 추출 ##############################

import sys, cv2, numpy as np

src = cv2.imread('./images/mnm.png')


if src is None:
    print("Image load failed")
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

## 트랙바 두개 만들어서, 최소/최대값 조절해서 색상영역 지정하기
def on_level_change(pos):
    hmin = cv2.getTrackbarPos('H_MIN', 'dst') # 트랙바의 위치를 받아옴 (h_min 값)
    hmax = cv2.getTrackbarPos('H_MAX', 'dst')

    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow("dst", dst)

# channel = cv2.split(src_hsv)
# h = channel[0]
# cv2.imshow('src', src)

# 윈도우창과 트랙바 생성
cv2.imshow("src", src)
cv2.namedWindow("dst")
cv2.createTrackbar("H_MIN", "dst", 50, 179, on_level_change) # h 최소값 설정
cv2.createTrackbar("H_MAX", "dst", 80, 179, on_level_change) # h 최대값 설정
on_level_change(0) # 이 코드가 없으면 위에서 설정한 영역이 바로 나오지 않음.
# 화면이 켜짐과 동시에 설정영역을 바로 나오게 하려면 이 코드가 필요함, 숫자는 상관없는 듯
cv2.waitKey()

# cv2.namedWindow("dst")
