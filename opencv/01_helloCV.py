import cv2
import sys
print("Hello openCV", cv2.__version__)

# 영상 파일 불러오기 
# cv2.IMREAD_GRAYSCALE : 흑백으로 불러오기
# cv2.IMREAD_UNCHANGED : 투명하게 불러오기

img = cv2.imread("./nacho.png") # 기본값은 컬러

# 흑백으로 불러오고 싶을 때
# img = cv2.imread("./nacho.png", cv2.IMREAD_GRAYSCALE)

# 이미지라는 이름의 새로운 창 만들기(사진 볼 새 창을 만든 것)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# cv2.WINDOW_AUTOSIZE : 자동크기 조절
# cv2.WINDOW_NORMAL : 사용자 크기조절 가능 

# 이미지가 만약 없을때 종료하기
if img is None:
    print("Image load failed!!")
    sys.exit()


# 이미지라는 창에 img 띄우기
cv2.imshow("image", img) # namedWindow가 없어도 창 띄우는 것은 가능하나 옵션을 줄 수 없다
# cv2.waitKey() # 키값이 들어올때 까지 기다리는 함수, 아무 키나 누르면 이미지 창이 닫힘
cv2.waitKey()
# waitKey()가 없으면 이미지창이 킴과 동시에 사라짐
# 반드시 있어야 이미지가 보인다. imshow와 waitKey는 하나의 쌍이다
# waitKey(2000) 2초 띄우고 사라짐(한 프레임에 2초 딜레이를 준것)
# key=cv2.waitKey() 키의 아스키값을 변수로 받아서 종료함 즉, 특정 키를 눌렀을때 종료하게 만들 수 있음
# print(key)



# waitKey() 를 활용한 창 종료 방법
# while True:
#      if cv2.waitKey() == 27: # esc가 입력되면 종료됨
#     # if cv2.waitKey() == ord('q'): # q 가 입력됐을 때 종료됨
#         break


#cv2.destroyAllWindows() # 모든 이미지창을 닫겠다
cv2.destroyWindow('image') # 이름이 image인 창을 닫겠다 

