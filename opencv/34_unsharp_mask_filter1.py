


import sys, cv2, numpy as np 

src = cv2.imread("./images/rose.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("failed")
    sys.exit()

blur = cv2.GaussianBlur(src, (0,0), 2)
# dst = src - blur
# dst = cv2.subtract(src, blur)

# 가중치를 주고 결과에 128을 더해줌으로써 눈으로 식별할수 있도록 함
# dst = cv2.addWeighted(src, 1, blur, -1, 128) # 엠보싱 효과

# 수식대로 배열 만들기, 실수로 표현해줘야함
dst = np.clip(2.0*src - blur, 0, 255).astype(np.uint8)



cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("blur", blur)
cv2.waitKey()
cv2.destroyAllWindows()
