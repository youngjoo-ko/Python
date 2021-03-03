

## 허프변환을 이용한 원 검출 함수
# cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None) 
'''
• image: 입력 영상. (에지 영상이 아닌 일반 영상 , 왜 ? 엣지이면 벡터계산을 할 수 없으므로)
• method: OpenCV 4.2 이하에서는 cv2.HOUGH_GRADIENT만 지정 가능
• dp: 입력 영상과 축적 배열의 크기 비율. 1이면 동일 크기. 2이면 축적 배열의 가로, 세로 크기가 입력 영상의 반.
• minDist: 검출된 원 중심점들의 최소 거리
• circles: (cx, cy, r) 정보를 담은 numpy.ndarray. shape=(1, N, 3), dtype=np.float32
• param1: Canny 에지 검출기의 높은 임계값
• param2: 축적 배열에서 원 검출을 위한 임계값
-> param1 값이 결정되면 낮은 임계치값은 자동으로 1/2로 결정된다.
-> param2 값에 따라 많은 원이 검출될 수 있고, 되지 않을 수도 있음
• minRadius, maxRadius: 검출할 원의 최소, 최대 반지름
'''

import sys, cv2, numpy as np

def on_trackbar(pos):
    rmin = cv2.getTrackbarPos("minRadius", 'img')
    rmax = cv2.getTrackbarPos("maxRadius", 'img')
    th = cv2.getTrackbarPos("threshold", 'img')
    pa1 = cv2.getTrackbarPos("param1", 'img')

    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 40, param1=pa1, param2=th, minRadius=rmin, maxRadius=rmax)

    dst = src.copy()

    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(dst, (cx, cy), radius, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow("img", dst)


src = cv2.imread("./images/phone.png")

if src is None:
    print("image load failed")
    sys.exit()


# # 블러처리해서 노이즈 제거하면 성능이 좋아짐
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0,0), 1.0)


# 트랙바 생성
cv2.imshow("img", src)

cv2.createTrackbar("minRadius", "img", 0, 100, on_trackbar)
cv2.createTrackbar("maxRadius", "img", 0, 150, on_trackbar)
cv2.createTrackbar("threshold", "img", 0, 100, on_trackbar)
cv2.createTrackbar("param1", "img", 0, 250, on_trackbar)
cv2.setTrackbarPos("minRadius", "img", 8)
cv2.setTrackbarPos("maxRadius", "img", 80)
cv2.setTrackbarPos("threshold", "img", 40)
cv2.setTrackbarPos("param1", "img", 125)

cv2.waitKey()
cv2.destroyAllWindows()