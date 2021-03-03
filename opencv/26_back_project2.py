
import sys, cv2, numpy as np


src = cv2.imread("./images/sheep.png")

if src is None:
    print("failed")
    sys.exit()

# CrCb의 살색 히스토그램을 얻어오기
reference_img = cv2.imread("./images/son_color.png")
mask = cv2.imread("./images/son_mask.bmp", cv2.IMREAD_GRAYSCALE)

ref_ycrcb = cv2.cvtColor(reference_img, cv2.COLOR_BGR2YCrCb)
channels = [1,2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128,128], ranges)

hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

### 기성용 이미지에 손흥민 마스크를 적용하여 얼굴(살색)만을 가져오는지
src = cv2.imread("./images/ki_color.png")

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

back_proj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

### 메시 이미지에 적용해보기
# 피부색이 다르기때문에 선명하게 가져오지 못함
messi = cv2.imread("./images/messi.png")

messi_ycrcb = cv2.cvtColor(messi, cv2.COLOR_BGR2YCrCb)

back_proj = cv2.calcBackProject([messi_ycrcb], channels, hist, ranges, 1)

cv2.imshow("src", src)
cv2.imshow("hist_norm", hist_norm) 
cv2.imshow("back_proj", back_proj)
cv2.imshow("messi", messi)
cv2.waitKey()
cv2.destroyAllWindows()