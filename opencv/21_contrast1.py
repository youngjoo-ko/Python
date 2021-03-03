
import sys, cv2, numpy as np

src = cv2.imread("./images/woman.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("failed")
    sys.exit()


## 명암비를 수동으로 조절하는 수식
# dst(x,y) = saturate((1+alpha) * src - 128*alpha)
alpha = 2.0 # 1로하면 안됨 , 커질수록 명암비는 커짐
# np.clip 함수를 이용하면 0이하, 255이상은 0 또는 255로 처리한다
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8) 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()