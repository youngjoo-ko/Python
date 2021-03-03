
# 영상의 속성
import cv2

# 이 때 img1의 타입은 numpy.ndarray 이다
# openCV는 영상데이터를 표현할 때 numpy.ndarray로 표현
img1 = cv2.imread('./nacho.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./nacho.png')

# 타입 알아보기
print(type(img1))

# shape 알아보기(세로,가로, 오픈cv는 뒤바껴서 표현되기 때문)
print(img1.shape)
print(img2.shape)

# dtype 알아보기
print(img2.dtype)

# 2차원이라는 말이므로 흑백이라는 뜻!
if len(img1.shape) == 2:
    print("img1은 그레이스케일")
elif len(img1.shape) == 3:
    print("img1은 트루컬러")

# img2의 이미지 사이즈 출력하기
h = img2.shape[0]
w = img2.shape[1]
h2, w2 = img1.shape
# h,w = img2.shape[:2]
print("img2의 사이즈는 {} * {}".format(w,h))
print("img1의 사이즈는 {} * {}".format(w2, h2))

# 영상의 픽셀값 참조
# x, y 는 좌표값
x = 20
y = 10
p1 = img1[y,x]
p2 = img2[y,x]
print(p1)
print(p2) # BGR 값이 리스트로 나옴

# 영상에 값을 넣어보기
#img1[y,x] = 0 # 해당 좌표에 검은점 찍기
img2[y,x]=(0,0,255) # 빨간점 찍기 

# 전체 이미지 색깔 바꾸기
img1[:,:] = 255 # 흰색
img2[:,:] = (0, 255, 255) #노란색

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey()
cv2.destroyAllWindows()



