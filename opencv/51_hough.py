

import sys, cv2, numpy as np

### 허프변환에 의한 직선 검출 
## cv2.HoughLines(image, rho, theta, threshold, lines=None, srn=None, stn=None, min-theta=None, max-theta=None)
# image : 엣지 입력 영상(canny 연산을 이용한 엣지 영상)
# rho : 축적배열에서 rho값의 간격(일반적으로 1.0을 넣어줌)
# theta : 축적배열에서의 theta값의 간격(np.pi/180) 
#- rho, theta 값이 커지면 축적배열의 크기가 작아짐.
#- 축적배열이 작아지면 정교한 직선을 표현하기 어렵다.
#- 축적배열이 커지면 정교한 직선표현이 가능하나 연산이 오래걸린다.

# threshold : 축적 배열에서 직선으로 판단할 임계값
#- 임계값을 낮추면 많은 직선이 검출된다.

# lines: 직선 파라미터(rho, theta) 정보를 담고 있는 3차원 행렬(numpy.ndarray, shape=(N, 1, 2), dtype=numpy.float32)
#- shape=(N, 1, 2)에서 1에는 쓸모 없는 값이 들어감.

# srn, stn: 멀티 스케일 허프 변환에서 rho 해상도, theta 해상도를 나누는 값. 기본값은 0이고, 이 경우 일반 허프 변환 수행.
# min_theta, max_theta: 검출할 선분의 최소, 최대 theta 값

### 확률적 허프 변환 함수
## cv2.HoughLinesP(image, rho, theta, threshold, lines=None, minLineLength=None, maxLineGap=None)
# image : 엣지 입력 영상(canny 연산을 이용한 엣지 영상)
# rho : 축적배열에서 rho값의 간격(일반적으로 1.0을 넣어줌)
# theta : 축적배열에서의 theta값의 간격(np.pi/180) 
# threshold : 축적 배열에서 직선으로 판단할 임계값
# lines : 선분의 시작과 끝 좌표(x1, y1, x2, y2) 정보를 담고있는 numpy.ndarray
# shape : (N, 1, 4) 좌표가 4개라서 4 , dtype=numpy.int32
# minLineLength : 검출하기 위한 성분의 최소 길이
# maxLineGap : 직선으로 간주하기 위한 최대 엣지점 간격


src = cv2.imread("./images/canny1.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("image load failed")
    sys.exit()

edges = cv2.Canny(src, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180.,120, minLineLength=50, maxLineGap=10)
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1]) # 시작점 좌표, 가운데값은 무조건 0으로!
        pt2 = (lines[i][0][2], lines[i][0][3]) # 끝점 좌표, 가운데값은 무조건 0
        cv2.line(dst, pt1, pt2, (0,255,0), 2, cv2.LINE_AA)


cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()