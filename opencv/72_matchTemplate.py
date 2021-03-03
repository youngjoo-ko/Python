import sys
import numpy as np
import cv2


# 입력 영상 & 템플릿 영상 불러오기
src = cv2.imread('./images/baseball_logo.png', cv2.IMREAD_GRAYSCALE)
templ = cv2.imread('./images/kia_logo.png', cv2.IMREAD_GRAYSCALE)

if src is None or templ is None:
    print('Image load failed!')
    sys.exit()


noise = np.zeros(src.shape, np.int32)
cv2.randn(noise, 50, 10) # 밝기 증가

src = cv2.add(src, noise, dtype=cv2.CV_8UC3)

res = cv2.matchTemplate(src, templ, cv2.TM_CCORR_NORMED)
## TM_SQDIFF, TM_SQDIFF_NORMED는 최소값을 택하고, 그 이외는 최대값을 택한다
# TM_CCORR 으로 설정할 경우 맨 오른쪽 상단(로고가 없는부분, 배경이 흰색이라 제일 밝으므로)을 캐치함
# TM_SQDIFF 로 설정할 경우 가장 어두운 부분을 택해야 하므로 아래 코드에서 min값을 택해야 한다
print(res) # 픽셀들의 값이 엄청 커져있는 것을 확인할 수 있다

res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# 이건 왜?
# cv2.TM_CCOEFF 혹은 cv2.TM_CCOEFF_NORMED의 경우 res값의 범위는 -1~1사이의 실수행렬이 나온다
# 0~1사이의 값이 될 수 있도록 정규화 해준것!
# 이 두개의 방법이 아니더라도 정규화를 해줘야 맵이 나왔을때 템플릿 영역과 아닌 영역의 구분이 가능하다
minv, maxv, minloc, maxloc = cv2.minMaxLoc(res)
# minv2, maxv2, minloc2, maxloc2 = cv2.minMaxLoc(res_norm)
print('maxv:', maxv)
print('maxloc:', maxloc)


th, tw = templ.shape[:2]
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
# TM_SQDIFF, 
# cv2.rectangle(dst, minloc, (minloc[0] + tw, minloc[1] + th), (0, 0, 255), 2)
cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)


cv2.imshow('src', src)
# cv2.imshow('res', res)
cv2.imshow('res_norm', res_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()