
# 그래디언트(x, y의 각각의 미분을 묶은 것!!)
'''
x,y축의 각 편미분값을 검출하여 벡터형태로 표현한 것
그래디언트 크기 : 픽셀 값의 차이 정도, 변화량에 따라 길이가 길어진다(벡터의 크기)
그래디언트 방향: 픽셀 값이 가장 급격하게 증가하는 방향
'''

## 2D 벡터 크기 구하는 함수
# cv2.magnitude(x, y, magnitude=None)
# x : 2D 벡터의 x 좌표 행렬(실수형), x의 편미분 값
# y : 2D 벡터의 y 좌표 행렬(실수형), y의 편미분 값


import sys, cv2, numpy as np

src = cv2.imread("./images/woman.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("image load failed")
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 1, 0)

dxy = cv2.magnitude(dx, dy, magnitude=None) # 급격하게 어두워진 부분들은 미분값이 마이너스가 나오면서 0에 가까워지고
# 밝아진 부분들은 255보다 큰값이 나오면 255에 가까워지기 때문에 노이즈현상처럼 출력됨

dxy = np.clip(dxy, 0, 255).astype(np.uint8) # situration 적용하여 원래 색상을 되찾도록 함!

# dxy 사이즈와 같은 검은 화면 생성
edge = np.zeros(dxy.shape[:2], np.uint8)

# 엣지를 범위 설정을 위한 임계값 설정
edge[dxy > 250] = 255  
# 색상값이 100보다 큰 경우 흰색으로 만들어줌
# 임계값이 낮을수록 더 많은 픽셀들이 흰색으로 바뀜 
# 임계값이 높을수록 엣지의 두께가 얇아짐, 엣지는 중간에 잘리는 현상 발생
# 임계값만으로 엣지를 찾으면 조명에 의해 픽셀이 받는 영향에 따라 엣지인데 못찾거나, 엣지가 아닌데 엣지로 표현하는
# 오류가 발생하기도 한다.

# 이를 해결하기 위해 canny 엣지 검출방식을 쓴다
# canny는 실제 엣지의 중심을 검출한다.


cv2.imshow("src", src)
cv2.imshow("dxy", dxy)
cv2.imshow("edge", edge)

cv2.waitKey()
cv2.destroyAllWindows()

