
import sys, cv2, numpy as np

src = cv2.imread("./images/woman.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("image load failed")
    sys.exit()

# x방향 미분을 위한 sobel 필터 배열 생성
###################################################################
# kernel_x = np.array([[-1, 0, 1],
#                    [-2, 0, 2],
#                    [-1, 0, 1]], dtype=np.float32)

# kernel_y = np.array([[-1, -2, -1],
#                      [0, 0, 0],
#                      [1, 2, 1]], dtype=np.float32)

# 2d 필터함수에 대입
# dx = cv2.filter2D(src, -1, kernel)
# dx1 = cv2.filter2D(src, -1, kernel_x, delta = 128) # delta값에 일정값을 더해줘서 처음에 안보였던 엣지를 보이게 해준다.
# dx2 = cv2.filter2D(src, -1, kernel_y) 

################### 직접 만드는것은 번거롭고 복잡함 ####################


## 편리하게 sobel함수 사용하자!
# cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)
# src : 입력영상
# ddepth : 출력영상의 데이터 타입(-1이면 입력영상과 같다, cv2.CV_32F로 연산하는 것이 일반적)
# dx : x방향의 미분차수 (1차 또는 2차 지정)
# dy : y방향의 미분차수
# dx = 1, dy=0 (x방향)/ dx=0, dy=1 (y방향) 로 설정하는것이 일반적
# ksize는 보통 3으로 지정
# scale : 연산결과에 추가적으로 곱할 값(기본값은 1)
# delta : 연산결과에 추가적으로 더할 값(기본값은 0)
# borderType : 가장 자리 픽셀의 확장 방식 (기본값은 cv2.BORDER_DEFAULT)


## 샤를필터도 있음, 매개변수는 동일
# cv2.Scharr(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)


# 소벨함수를 이용한 x,y 방향 미분(편미분만 가능)
dx = cv2.Sobel(src, -1, 1, 0)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

# dxy = cv2.Sobel(src, -1, 1, 1, delta=128) # 양방향을 한번에 표현하는 것은 불가!

cv2.imshow("src", src)
# 배경에 있는 거울 아치에 엣지가 없는 이유
# 회색(밝은색) -> 검은색(어두운색) 이므로 미분값(변화량, 기울기)이 음의값이 나온것이다.
# 이는 situration에 의해 0에 가까워지고, 검은색으로 표시된 것이다.
# cv2.imshow("dx1", dx1)
# cv2.imshow("dx2", dx2)
cv2.imshow("dx", dx)
cv2.imshow("dy", dy)

cv2.waitKey()
cv2.destroyAllWindows()