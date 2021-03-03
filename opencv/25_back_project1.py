

########################### 히스토그램 역투영 ##############################

## 히스토그램 역투영 함수
# cv2.calcBackProject(images, channels, hist, ranges, 
# images: 입력 영상 리스트
# channels: 역투영 계산에 사용할 채널 번호 리스트
# hist: 입력 히스토그램 (numpy.ndarray)
# ranges: 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
# scale: 출력 역투영 행렬에 추가적으로 곱할 값
# dst: 출력 역투영 영상. 입력 영상과 동일 크기, cv2.CV_8U.)

## 특정영역 선택하는 함수
# cv2.selectROI(src)

import sys, cv2, numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("./images/sheep.png")

if src is None:
    print("failed")
    sys.exit()


# ROI selextor 창 생성
x, y, w, h = cv2.selectROI(src) # 특정영역을 지정할 수 있는 창이 하나 뜸, 리턴값은 x,y좌표와 w,h 너비, 폭

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
channels = [1,2] # 0인덱스인 y 성분은 쓰지 않음. y 성분은 밝기 정보.
hist_size = [128, 128] # 왜 128?
cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

# 선택 영역의 히스토그램 생성
crop_zone = src_ycrcb[y:y+h, x:x+w]
hist = cv2.calcHist([crop_zone], channels, None, hist_size, ranges) # 히스토그램으로 나타낼 수 있는 채널은 cr, cb 두개

# 히스토그램 스트레칭
hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
print(hist_norm.shape)
# norm_chart = getHistDraw(hist_norm)

# 입력영상 전체에 대한 히스토그램 역투영
back_proj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
dst = cv2.copyTo(src, back_proj) # 마스크 연산해서 해당 영역만 원본에 표현

# plt.plot("hist_norm",hist_norm)
# plt.show()
cv2.imshow("hist_norm", hist_norm) # 초원의 히스토그램
cv2.imshow("back_proj", back_proj)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()