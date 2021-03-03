
import sys, cv2, numpy as np


src = cv2.imread("./images/sheep.png")

if src is None:
    print("failed")
    sys.exit()

def getHistDraw(hist):
    imgHist = np.full((100,128), 255, dtype=np.uint8) # 흰색배경의 행렬 생성 
    histMax = np.max(hist)
    
    for x in range(128):
        pt1 = (x, 100)   # 행렬이기 때문에 시작점(0,0)은 히스토그램 좌측 상단이다, y축 좌표는 밑으로갈수록 커짐
        pt2 = (x, 100 - int(hist[x,0]*100/histMax)) # 끝점, 100을 곱하고 255로 나눠 단위 통일
        cv2.line(imgHist, pt1, pt2, 0) # 직선을 그려 히스토그램 그리기
    
    return imgHist


# CrCb의 살색 히스토그램을 얻어오기
reference_img = cv2.imread("./images/son_color.png")
mask = cv2.imread("./images/son_mask.bmp", cv2.IMREAD_GRAYSCALE)


ref_ycrcb = cv2.cvtColor(reference_img, cv2.COLOR_BGR2YCrCb) # 3차원 
channels = [1,2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128,128], ranges)

hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)



### 기성용 이미지에 손흥민 마스크를 적용하여 얼굴(살색)만을 가져오는지
src = cv2.imread("./images/ki_color.png")

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

back_proj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)


# 채널별 분리
ycrcb_channels = cv2.split(reference_img)
##################################################채널별 히스토그램 만들기 
hist_cr = cv2.calcHist([ycrcb_channels[1]], [0], None, [128], [0,128])
cr_chart = getHistDraw(hist_cr)
hist_cb = cv2.calcHist([ycrcb_channels[2]], [0], None, [128], [0,128])
cb_chart = getHistDraw(hist_cb)
########################################################################


### 메시 이미지에 적용해보기
# 피부색이 다르기때문에 선명하게 가져오지 못함
messi = cv2.imread("./images/messi.png")

messi_ycrcb = cv2.cvtColor(messi, cv2.COLOR_BGR2YCrCb)

back_proj = cv2.calcBackProject([messi_ycrcb], channels, hist, ranges, 1)


cv2.imshow("src", src)
cv2.imshow("hist_norm", hist_norm) 
cv2.imshow("cr_chart", cr_chart) 
cv2.imshow("cb_chart", cb_chart) 

cv2.imshow("back_proj", back_proj)
cv2.imshow("messi", messi)
cv2.waitKey()
cv2.destroyAllWindows()