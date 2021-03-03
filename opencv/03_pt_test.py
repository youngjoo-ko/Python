import sys
import cv2
import glob

# images 폴더에 있는 모든 jpg 파일 불러오기
imgs = glob.glob("./images/*.jpg")

# for f in imgs:
#     print(f)

# 이미지를 전체화면으로 띄우기
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 어떤 키를 누를때까지 이미지 무한으로 띄우기
cnt = len(imgs)
idx = 0

while 1:
    img = cv2.imread(imgs[idx])

    if img is None:
        print("image load failed !!")
        break
    
    cv2.imshow("image", img)

    # 어떤 키값이 들어온다는 건 0보다 큰것이기 때문에 이렇게 설정
    if cv2.waitKey(1000) >= 0:
        break
    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()