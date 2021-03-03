
import sys, cv2, numpy as np, matplotlib.pyplot as plt

src = cv2.imread("./images/test_coin1.jpg")

if src is None:
    print("image load failed")
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0,0), 1)

# 허프변환 원 검출 함수 사용(리턴값은 검출된 원들의 정보를 가진 np.ndarray(cx, cy, radius) )
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=140, param2=42, minRadius=20, maxRadius=50)
print(circles.shape)
# print(circles[0][0].shape) # circles는 검출된 원의 (x , y 좌표, 반지름)을 가진 배열을 리턴한다 
# print(circles.shape) # (1, n, 3) 여기서 n은 원의 개수, 3은 정보 3가지
# 원 검출 결과 및 동전금액 출력하는 코드
sum_of_coin = 0 # 동전 합계금액
dst = src.copy() # 원본 컬러 이미지 복사

if circles is not None:
    for i in range(circles.shape[1]): # 동전 개수만큼(N개)
        cx, cy, radius = circles[0][i] # 앞에 0은 무조건 들어감?
        cv2.circle(dst, (cx,cy), radius, (255,0,255), 1,  cv2.LINE_AA) # 찾은 원에 대해 순서대로 보라색 써클을 그림
        cv2.circle(dst, (cx,cy), 2, (0,0,255), 5)

        # 각 동전 영역 부분 영상 추출
        x1 = int(cx - radius)
        y1 = int(cy - radius)
        x2 = int(cx + radius)
        y2 = int(cy + radius)
        
        print(radius)

        crop = dst[y1:y2, x1:x2, :]
        ch, cw = crop.shape[:2] # 세로 가로 추출

        # 동전 영역에 대한 ROI 마스크 영상 생성
        mask = np.zeros((ch, cw), np.uint8)
        cv2.circle(mask, (cw//2, ch//2), radius, 255, -1)
        # masked = cv2.bitwise_and(crop, mask)

        # hue 계산
        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        hue,s,v = cv2.split(hsv)
        hist_shift = (hue + 50) % 180 # 빨간색인경우, 히스토그램의 양 끝단에 모두 표현되기 때문에 평균에 영향을 미침 
        # 50을 더해줘서 왼쪽으로 땡겨와서 표현하는 것이다....ㅠㅠ
        mean_of_hue = cv2.mean(hist_shift, mask)[0]
        print(mean_of_hue) # 여기서 나오는 수치에 따라 밑에 if문 mean_of_hue 값을 바꿔주면 된다

        # histogram = cv2.calcHist([hue], [0], None, [180], [0,180])
        # plt.hist(hue, 256, [0,256])
        
        # plt.plot(histogram)
        cv2.imshow("crop", crop)
        cv2.imshow("mask", mask)
        # plt.show()
        cv2.waitKey()

        # hue 평균이 58보다 작으면 10원, 크면 100원으로 간주
        won = 100
        if mean_of_hue < 58:
            won = 10
        elif mean_of_hue > 131:
            if radius >= 44:
                won = 500
            elif radius <= 36.6:
                won = 50
        
        sum_of_coin += won

        cv2.putText(crop, str(won), (20,50), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255,0,0), 2, cv2.LINE_AA)

cv2.putText(dst, str(sum_of_coin) + "won", (40, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 2, cv2.LINE_AA)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()