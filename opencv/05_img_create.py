
import numpy as np
import cv2

# 영상 생성하기(세로, 가로 )
# zeros : 0으로 초기화된 shape 차원의 nparray를 반환
# ones : 1로 초기화
# full : 모든값을 full 10으로 초기화
# img1 = np.empty((240, 320), dtype=np.uint8) # 2차원으로 지정했기 때문에 type은 grayscale
img2 = np.zeros((240, 320, 3), dtype=np.uint8) # color
print(img2.shape)
# img3 = np.ones((240, 320), dtype=np.uint8) # grayscale
img4 = np.full((240, 320, 3), (0,255,0), dtype=np.uint8) # 원하는 색상으로 
print(img4.shape)
# print(img1.shape)

# cv2.imshow("img1", img1) # 쓰레기값이 들어있기 때문에 매번 다른 이미지가 출력됨
# cv2.imshow("img2", img2) # 쓰레기값이 들어있기 때문에 매번 다른 이미지가 출력됨
# cv2.imshow("img3", img3) # 쓰레기값이 들어있기 때문에 매번 다른 이미지가 출력됨
# cv2.imshow("img4", img4) 
# cv2.waitKey()
# cv2.destroyAllWindows()

 # 영상 복사하기
# img1 = cv2.imread("./nacho.png")
# img2 = img1 # img1을 참조함
# img3 = img1.copy() # 새로운 메모리에 할당한 복사본

# # img1[:, :] = (0, 255, 0) # img2도 이 코드의 영향을 받음

# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.imshow("img3", img3) 
# cv2.waitKey() 

# 부분적 영상 추출
img1 = cv2.imread("./nacho.png") # 사이즈 487, 703, 3 (세로, 가로)
# 세로 가로
img2 = img1[120:220, 180:380] # 데이터가 numpy.ndarray 이기 때문에 슬라이싱이 가능하다
img3 = img1[120:220, 180:380].copy()

# img1[:, :] = (0, 255, 0)
# img2.fill(0) # 잘라온 부분에 값을 채웠을 때 참조본에도 값이 채워진다

# 좌표, 반지름, 색상, 두께
cv2.circle(img2, (20, 20), 10, (0, 0, 255), 2) # 잘라온 부분에 원을 그리면 참조본에도 적용됨

cv2.imshow("img1", img1) # green
cv2.imshow("img2", img2) # 부분적 green
cv2.imshow("img3", img3)
cv2.waitKey() 