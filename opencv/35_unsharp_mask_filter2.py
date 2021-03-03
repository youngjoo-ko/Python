

#################### 컬러 영상에 대한 언샤프 마스크 필터링 적용 #####################

import sys, cv2, numpy as np 

src = cv2.imread("./images/rose.png")

if src is None:
    print("failed")
    sys.exit()


# ycrcb로 바꾸고 채널 분리
ycrcb_src = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# y성분만 추출하여 블러처리, 이 중간과정의 연산에선 실수가 좋다 
# float32올 conversion 하는 이유 : 중간과정에서 미세한 계산치가 사라지지 않도록 하기위함
# 내부연산을 한 후에 최종결과를 확인할 때는 uint8로 형변환하는 것이 좋다.
y_channel = ycrcb_src[:, :, 0].astype(np.float32) 
blur = cv2.GaussianBlur(y_channel, (0,0), 2)

# 블러처리한것을 수식에 넣어 새로운 그래프를 만들고, 이를 다시 원본에 넣어주고 수식대로 배열 만들기, 최종은 uint8로
ycrcb_src[:,:,0] = np.clip(2.0*y_channel - blur, 0, 255).astype(np.uint8)

# 영상 출력을 위해 bgr로 변환
dst = cv2.cvtColor(ycrcb_src, cv2.COLOR_YCrCb2BGR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()
