import cv2
 

########################################## 영상 합성 ############################################

# ROI(Region of Interest) : 관심영역
# : 영상에서 어떤 특정한 연산을 수행하고자 할 때 사용하는 임의의 부분 영역

# 마스크 이미지 : 검은색과 흰색으로 이루어진 (보통 사물은 흰색, 여백은 검은색으로 채우는)
# 흰색은 불투명, 검은색은 투명으로 처리됨

# 마스크 연산을 하기위한 함수 : 복사를 해주는 함수 
# cv2.copyTo(src, mask, dst) : 세개의 사이즈는 같고, src와 dst의 타입은 같아야한다(트루컬러 혹은 그레이스케일)
# src : 입력영상
# mask : 마스크 영상(0이 아닌 값(픽셀)에 대해서만 연산을 수행(복사))
# dst : 출력 영상

src = cv2.imread("./images/airplane.bmp")
mask = cv2.imread("./images/mask_airplane.bmp", cv2.IMREAD_GRAYSCALE)
dst = cv2.imread("./images/field.bmp")

# 1. copyTo 함수 사용하기
# cv2.copyTo(src, mask, dst)
# cv2.imshow("src", src)
# cv2.imshow("mask", mask)
# cv2.imshow("dst", dst)

# 2. numpy의 boolean 인덱싱을 이용하기
# dst[mask > 0] = src[mask > 0] # 즉, mask의 흰색 부분만큼만 떼어와서 새로운 이미지에 그 위치에 합성하겠다/ 

# 3. 알파채널이 있는 영상을 합성하기
# 알파채널(마스크 채널) ? RGBA는 RGB에 A(알파, alpha)가 추가된 색상 표기법입니다. A는 배경의 투명도를 의미합니다. 
# A 역시 0~255의 값을 가질 수 있지만, 배경의 투명도를 표현하기 위해 0과 255만 사용하는 경우가 많습니다. 
# A값이 255면 흰색, 0이면 검은색입니다. 

### imread 함수의 두 번째 파라미터가 cv2.IMREAD_UNCHANGED인 경우 이미지가 알파 채널을 가지고 있는 경우 BGRA 방식으로 읽습니다.

logo = cv2.imread("./images/opencv.png", cv2.IMREAD_UNCHANGED) ### png는 투명배경을 지원한다
nacho = cv2.imread("./nacho.png")

mask = logo[:,:,3] # mask 는 알파채널로 만드는 역햘을 함(0,1,2 는 b,g,r, 3은 a)
print(mask.shape)

cv2.imshow('mask', mask)
cv2.waitKey()

logo = logo[:,:,:-1] # BGR만 가져오기 (마지막 mask를 빼고 슬라이싱 함)
logo = ~logo
cv2.imshow('logo', logo)
cv2.waitKey()

h, w = mask.shape[:2]

# src(로고이미지)와 dst(나초 이미지)의 크기가 다르다. 따라서 마스크 연산이 안됨
# src와 동일한 크기의 영상을 참조 => crop
crop = nacho[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출, 좌표는 임의대로

cv2.copyTo(logo, mask, crop) # 로고와 크롭은 같은 트루컬러 타입
#crop[mask > 0] = logo[mask > 0] # bool 인덱싱도 이용 가능


cv2.imshow("nacho", nacho)
# cv2.imshow("logo", logo)
# cv2.imshow("mask", mask)

cv2.waitKey()
cv2.destroyAllWindows()
