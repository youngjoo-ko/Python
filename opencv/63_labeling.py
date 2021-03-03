
### 레이블링 함수
## connectedComponents(image, label=None, connectivity = None, ltype=None) -> retval, labels 리턴
# image : 입력영상(8비트 1채널)
# labels : 입력영상과 같은 크기의 레이블 맵(numpy.ndarray)
# connectivity :  기본값은 8(이웃 연결관계)
# ltype : labels 타입, 기본값은 cv2.CV_32S, 또는 cv2.CV_16S
## retval : 객체의 개수 + 1(배경까지 포함), n을 반환하면 객체의 개수는 n-1개(배경하나를 빼준것)


## connectedComponentsWithStats(image, label=None, stats=None, centroids=None, connectivity = None, ltype=None) 
# -> retval, labels, stats, centroids 리턴
# stats : 바운딩박스(객체가 어느위치에 어떤 크기로 존재하는지, 픽셀의 개수는 몇갠지 갖고있는 행렬) 정보를 담고 있음
# stats의 shape=(N, 5) , dtype=np.int32
# centroids : 각 객체의 중심 위치 정보를 담은 행렬, shape=(N,2), dtype=bnp.float64
# ltype : labels 타입, 기본값은 cv2.CV_32S, 또는 cv2.CV_16S



import sys, cv2, numpy as np


mat = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)

cnt, labels = cv2.connectedComponents(mat)

print('sep:', mat, sep='\n')
print('cnt:', cnt)
print('labels:', labels, sep='\n')

