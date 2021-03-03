

########################### cv2.line() 함수로 히스토그램 그리기 #############################


import sys, cv2, numpy as np
import matplotlib.pyplot as plt

def getHistDraw(hist):
    imgHist = np.full((100,256), 255, dtype=np.uint8) # 흰색배경의 행렬 생성 
    histMax = np.max(hist)
    print(histMax)
    
    for x in range(256):
        pt1 = (x, 100)   # 행렬이기 때문에 시작점(0,0)은 히스토그램 좌측 상단이다, y축 좌표는 밑으로갈수록 커짐
        pt2 = (x, 100 - int(hist[x,0]*100/histMax)) # 끝점, 100을 곱하고 255로 나눠 단위 통일
        cv2.line(imgHist, pt1, pt2, 0) # 직선을 그려 히스토그램 그리기
    
    return imgHist


src = cv2.imread('./images/woman.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256]) # 1차원 배열(256,1)
print(hist)
hist_chart = getHistDraw(hist)

cv2.imshow('src',src)
cv2.imshow('hist_chart',hist_chart)
cv2.waitKey() # 1로 설정한 이유는 다음 matplot 명령어를 실행시키기 위함. 창은 사라지지 않음(?)

plt.plot(hist)
plt.show()
cv2.destroyAllWindows()