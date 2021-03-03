
## 컴퓨터 비전에서 연산시간 체크의 필요성
# 컴퓨터 비전은 대용량 데이터를 다루어서 의미있는 최종결과를 얻어내야 한다.
# 이를 위해서는 여러 단계를 거치게되는데, 매 단계에서 병목(bottleneck)현상이 있는지
# 체크하는 것은 중요한 과정이다.
# 단계별 연산시간을 체크하기 위해 사용하는 함수 TickMeter

import cv2
import sys
import numpy as np

img = cv2.imread("./images/big.jpg")

if img is None:
    print("failed")
    sys.exit()

# 특정 연산에 대한 시간 측정하기
tm = cv2.TickMeter()

tm.reset()
tm.start()

edge = cv2.Canny(img, 50, 150)

tm.stop()
print('elapsed time: {}ms'.format(tm.getTimeMilli())) # 87.3117ms(0.08초 정도 소요)
# 연산시간이 오래 걸리는 경우 어느부분에서 병목현상이 있는지 확인하고 없애주어야 연산시간을 줄일 수 있다
# 만약 졸음운전 모습을 캡쳐해서 경고해주는 서비스의 경우 시간이 경쟁력(느리면 사고의 위험율이 올라가므로)