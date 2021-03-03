# import cv2
 

# logo = cv2.imread("./images/cv_logo.png", cv2.IMREAD_UNCHANGED)
# img = cv2.imread("./images/robot.jpg")
# print(img.shape)


# mask = logo[:,:,3]

# logo = logo[:,:,:-1]

# h, w = mask.shape[:2]

# crop = img[400:400+h, 200:200+w]  

# cv2.copyTo(logo, mask, crop) # 로고와 크롭은 같은 트루컬러 타입

# cv2.imshow("img", img)
# cv2.waitKey()
# cv2.destroyAllWindows()



########################################################
import cv2
 

logo = cv2.imread("./images/cv_logo.png", cv2.IMREAD_UNCHANGED)
img = cv2.imread("./images/robot.jpg")
img2 = img.copy()
print(img.shape)

mask = logo[:,:,3]

logo = logo[:,:,:-1]

h, w = mask.shape[:2]

crop = img[400:400+h, 200:200+w]  

# cv2.copyTo(logo, mask, crop) # 로고와 크롭은 같은 트루컬러 타입
crop[mask > 0] = logo[mask > 0]
# 원본 img 가중치를 0.7로 , 크기조절 사각형이 그려진 cpy 가중치를 0.3으로 둘이 합침
img = cv2.addWeighted(crop, 0.9, logo, 0.1, 0)


cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
