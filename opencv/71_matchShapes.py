import sys
import numpy as np
import cv2


# 영상 불러오기
obj = cv2.imread('./images/heart.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/all.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or obj is None:
    print('Image load failed!')
    sys.exit()


# obj 영상의 이진화
_, obj_bin = cv2.threshold(obj, 128, 255, cv2.THRESH_BINARY_INV)

# 이진화된 영상 확인(객체가 흰색)
cv2.imshow('obj_bin', obj_bin)
cv2.waitKey(0)

# 외곽선 검출
obj_contours, _ = cv2.findContours(obj_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(obj_contours)) # 외곽선의 개수(하트 1개)
obj_pts = obj_contours[0] # 첫번째 외곽선, 즉 하트가 갖고있는 x,y좌표 전부
print(obj_pts)

# src(입력) 영상의 이진화
_, src_bin = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY_INV)

# 외곽선 검출
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 결과 영상
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 입력 영상의 모든 객체 영역에 대해서
for pts in contours:
    if cv2.contourArea(pts) < 1000: # 노이즈 제거
        continue

    # 찾은 외곽선에 대한 최내접 사각형의 좌표
    rc = cv2.boundingRect(pts)
    print(rc)
    # 사각형 빨간색으로 그리기
    cv2.rectangle(dst, rc, (0, 0, 255), 2)

    # 모양 비교, 비슷한 정도에 대해 거리값을 리턴(작으면 비슷)
    dist = cv2.matchShapes(obj_pts, pts, cv2.CONTOURS_MATCH_I3, 0)

    # 해당 외곽선 위에 거리값 쓰기
    cv2.putText(dst, str(round(dist, 4)), (rc[0], rc[1] - 3),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)

    '''
● cv2.putText(img, text, org, font, fontScale, color, thickness)
· img : 텍스트를 작성할 캔버스가 될 img
· text : 적고자 하는 텍스트 내용
· org : 문자열이 표시될 위치, bottom-left의 좌표점
· font : 폰트 타입
· fontScale : 폰트 크기
· color : 폰트 컬러
· thickness : 폰트 두께
'''

cv2.imshow('obj', obj)
cv2.imshow('dst', dst)
cv2.waitKey(0)