import sys
import numpy as np
import cv2

src = cv2.imread('./images/keyboard.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 레이블링을 위해 자동 이진화(오츠) 시킴
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)


# WithStats 함수를 이용해 레이블링하고, 객체의 개수 등 정보를 받아옴
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
print(cnt) # 40개, 노이즈 발생
print(stats[0]) # 2차원 행렬, stats[i] 첫번째 객체(배경)에 대한 바운딩 박스
print(centroids) # 2차원 행렬

# 노이즈 제거 후 정보 다시 받아오기
# dst_no = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)
# cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(dst_no)
# print(cnt) # 29개, 노이즈 삭제, 객체의 개수는 28개

# 아래코드에서 원본에 사각형을 그리기 위해 원본처럼 BGR로 변환
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt): # 객체의 바운딩박스 정보를 순서대로 꺼내옴
    (x, y, w, h, area) = stats[i] # 배경을 하나 빼야되므로 cnt까지 range 설정
    # print(area)
    if area > 20: # 열기 연산안하고 여기서 면적크기를 이용해 노이즈 제거 가능!
        cv2.rectangle(dst, (x, y, w, h), (255, 0, 255), 2) 


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()