

################################## 영상의 이동 #################################

import sys, cv2, numpy as np

src = cv2.imread("./images/sea.png")


if src is None:
    print("failed")
    sys.exit()

## 영상의 어파인 변환 함수
# cv2.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)
# src : 입력영상
# M : 2x3 변환행렬(실수형)
# dsize : 결과 영상 크기(w,h) 튜플로 표현 , (0,0) 이면 입력영상과 같은 크기로 설정한다는 뜻
# dst : 출력영상
# flags : 보간법을 설정하는 파라미터, 기본값은 cv2.INTER_LINEAR(양선형 보간법)
# 보간법 ? 결과 영상의 퀄리티를 보정하는 방법
# -cv2.INTER_NEAREST : 최근접 이웃 보간법, 효율성이 가장 낮음
# -cv2.INTER_LINEAR : 양선형 보간법, 퀄리티와 속도가 어느정도 보장되어 있음, 효율성이 가장 높음
# -cv2.INTER_CUBIC : 퀄리티는 리니어보다 약간 좋으나 속도가 느림(4*4)
# -cv2.INTER_LANCZOS4 : 퀄리티는 좋으나 속도가 느림(8*8)
# -cv2.INTER_AREA : 영상 축소 시 효과적으로 사용하는 방식
# borderMode: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT.
# borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0(검정색).


# 어파인 변환 행렬 생성(어파인 변환행렬은 2x3인 단위행렬)
aff = np.array([[1,0,300], # 가로 이동크기
               [0,1,200]], dtype=np.float32) # 세로 이동크기


# 이동(변환행렬을 변환함수에 대입)
dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
