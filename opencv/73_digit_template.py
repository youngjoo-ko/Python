import sys
import numpy as np
import cv2


def load_digits():
    # 템플릿 영상을 담을 리스트 생성
    img_digits = []

    # 0 ~ 9 까지의 템플릿 불러와서 리스트에 추가
    for i in range(10):
        filename = './images/digits/digit{}.bmp'.format(i)
        img_digits.append(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

        if img_digits[i] is None:
            return None

    return img_digits # 리스트 리턴


def find_digit(img, img_digits):
    max_idx = -1
    max_ccoeff = -1

    for i in range(10):
        # 입력 영상에서 잘라온 부분영상 리사이즈
        img = cv2.resize(img, (100, 150))

        # 1x1 행렬 리턴(입력영상에서 잘라온 영상과 템플릿 사이즈가 같으므로)
        res = cv2.matchTemplate(img, img_digits[i], cv2.TM_CCOEFF_NORMED)

        if res[0, 0] > max_ccoeff:
            max_idx = i
            max_ccoeff = res[0, 0]

        # cv2.imshow("img", img) # 1은 이상하게 리사이즈 됨
        # cv2.waitKey()
    return max_idx


def main():
    src = cv2.imread('./images/digits.bmp') # 입력영상

    if src is None:
        print('Image load failed!')
        return

    # 100x150 숫자 영상 불러오기
    img_digits = load_digits()  # list of ndarray
    print(img_digits)

    if img_digits is None:
        print('Digit image load failed!')
        return

    #  영상 이진화
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    # 레이블링 
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src_bin) 

    dst = src.copy()
    for i in range(1, cnt): # 배경 제외하고 객체 가져오기
        (x, y, w, h, s) = stats[i] # 바운딩 박스의 정보 변수에 담기
        print(s)
        if s < 700: # 면적이 1000보다 작은것 제외 (그럼 1도 제외? 700으로 낮추면 1도 가져옴)
            continue

        digit = find_digit(src_gray[y:y+h, x:x+w], img_digits)
        cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))
        cv2.putText(dst, str(digit), (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # 1이 9로잡히는 이유는 글씨체가 달라서

if __name__ == '__main__':
    main()