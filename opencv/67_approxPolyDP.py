
import math
import cv2

def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

def main():
    img = cv2.imread('./images/polygon.jpg', cv2.IMREAD_COLOR)    

    if img is None:
        print('Image load failed!')
        return

    # 그레이 스케일로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 이진화
    _, img_bin = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV) 
    # 임계값 왜 줬는지 ? 별은 노란색이라서 오츠로 잘 안잡히기떄문에

    # 외곽선 검출
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('img_bin', img_bin)
    cv2.imshow('gray', gray)

    for pts in contours:
        # 면적이 300 미만인 것들은 패스
        # print(cv2.contourArea(pts))
        if cv2.contourArea(pts) < 300:
            continue
        

        # 300 이상인것들의 외곽선 근사화
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
        print(approx)
        # approx는 근사화된 꼭지점 좌표의 배열
 
        convex_is = cv2.isContourConvex(approx)
        vtc = len(approx) # vtc는 꼭지점의 개수
        print(convex_is)

        if convex_is:
            if vtc == 3:
                setLabel(img, pts, 'TRI')
            elif vtc == 4:
                setLabel(img, pts, 'RECT')
            elif vtc == 5:
                setLabel(img, pts, 'PENTAGON')
        
            else:
                length = cv2.arcLength(pts, True)
                area = cv2.contourArea(pts)
                ratio = 4. * math.pi * area / (length * length)

                if ratio > 0.85:
                    setLabel(img, pts, 'CIR')
                elif ratio < 0.85:
                    setLabel(img, pts, 'ellipse')
        else:
            continue

    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()