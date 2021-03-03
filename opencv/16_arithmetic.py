
# 산술 연산
## cv2.add , cv2.subtract, cv2.addEeighted, cv2.absdiff 

## cv2.addWeighted(src1, alpha, src2, gamma, dst, dtype)
# src1, src2 : 입력영상들
# dst : 출력 영상
# alpha : 첫번째 영상의 가중치 (투명도)
# beta : 두번째 영상의 가중치
# gamma : 결과 영상에 추가적으로 더해줄 값
# dtype : 보통생략, 출력영상 타입




import sys, cv2, numpy as np

src1 = cv2.imread("./images/gray_woman.bmp")
src2 = cv2.imread("./images/square.bmp")
src3 = cv2.imread("./images/hole.bmp")

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U) # uint8 타입으로 불러옴
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2) # saturate 연산된 것 (src1-src2를 뺀것)
dst4 = cv2.absdiff(src1, src2) # src1 - src2의 절대값(픽셀)을 영상에 반영함


dst5 = cv2.subtract(src1, src3)
dst6 = cv2.add(src1, src3)

# cv2.imshow("dst1", dst1)
# cv2.imshow("dst2", dst2)
# cv2.imshow("dst3", dst3)
# cv2.imshow("dst4", dst4)
cv2.imshow("dst5", dst5)
cv2.imshow("dst6", dst6)
cv2.waitKey()