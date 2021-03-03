
################ 영상 다운 샘플링 #######################
## cv2.pyrDown(src, dst, dstsize, borderType)
# src : 입력영상
# dst : 출력영상
# dstsize : 출력영상 사이즈 , 설정하지 않는 경우 입력영상의 가로, 세로 1/2 크기로 설정됨(원본의 1/4)



import sys, cv2, numpy as np 

src = cv2.imread("./nacho.png")

if src is None:
    print("failed")
    sys.exit()

# 강아지 얼굴 인식위한 사각형 그리기
rc = (350,50,150,150)
cpy = src.copy()
cv2.rectangle(cpy, rc, (0,0,255), 2)
cv2.imshow("src_origin", cpy)
cv2.waitKey()


for i in range(1,4):
    src = cv2.pyrDown(src)
    cpy = src.copy()

    cv2.rectangle(cpy, rc, (0,0,255), 2, shift = i)
    cv2.imshow("src_copy", cpy)
    cv2.waitKey()
    cv2.destroyAllWindows()

cv2.destroyAllWindows()