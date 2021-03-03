
### 모폴로지 연산 함수
## cv2.morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
# op : 모폴로지 연산 플래그
#- cv2.MORPH_ERODE : 침식
#- cv2.MORPH_DILATE : 팽창
#- cv2.MORPH_OPEN : 침식 후 팽창(열기, 잡음제거)
#- cv2.MORPH_CLOSE : 팽창 후 침식(닫기)
#- cv2.MORPH_GRADENT : 팽창 - 침식import sys, cv2, numpy as np



import sys, cv2, numpy as np

src = cv2.imread("./images/rice.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("lmage load failed!")
    sys.exit()


##################### 지역 이진화 #####################################
dst = np.zeros(src.shape, np.uint8)

# 입력 영상을 가로, 세로로 4등분(총 16등분)
bw = src.shape[1] // 4 # 분할한 사각형의 가로 사이즈
bh = src.shape[0] // 4 # 분할한 사각형의 세로 사이즈

for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst[y*bh:(y+1)*bh, x*bw:(x+1)*bw]

        # dst_를 파라미터로 사용하면 입력 및 출력으로 사용할 수 있다
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)
#################################################################################

'''
# cv2.connectedComponents(dst) : 흰색 객체의 개수와 labels를 리턴함
cnt, _ = cv2.connectedComponents(dst) 
print(cnt) # 133개, 잡음제거 전이므로 잡음의 개수까지 포함된다.

# 열기연산으로 쌀알이외에 노이즈 제거,(원래 쌀알을 작아졌다가 팽창후 커진다)
dst2 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, None)
cnt2, _ = cv2.connectedComponents(dst2)
print(cnt2) # 99개
'''
# 위 코드를 다른 방법으로(침식과 팽창을 따로)
# 침식
dst1 = cv2.erode(dst, None) # None은 커널사이즈 기본값 3,3

# 팽창
dst2 = cv2.dilate(dst1, None)


cv2.imshow("src", src)
# cv2.imshow("dst", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2) # 잡음이 제거되었다

cv2.waitKey()
cv2.destroyAllWindows()
