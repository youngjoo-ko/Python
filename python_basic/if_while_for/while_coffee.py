coffee = 10
money = 300
while money:
    print('커피가 나옵니다')
    coffee = coffee - 1
    print('남은 커피는 %d잔입니다' %coffee)
    if coffee == 0:
        print('커피가 품절되었습니다. 판매를 중지합니다.')
        break


meet = 0
while meet < 4 :
    meet += 1
    print("유비가 %d번 방문했습니다." %meet)
    if meet == 3:
        print("제갈량이 유비곁으로 갑니다.")
        break
