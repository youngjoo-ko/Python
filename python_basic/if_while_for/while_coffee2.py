coffee = 10
while True:
    money = int(input('돈을 넣어주세요: '))
    if money == 300:
        print('커피가 나옵니다')
        coffee = coffee - 1
        print('남은 커피는 %d잔 입니다.' %coffee)
    elif money > 300:
        print('커피가 나오고, 거스름돈 %d를 돌려줍니다.' %(money-300))
        coffee = coffee - 1
        print('남은 커피는 %d잔 입니다.' %coffee)
    else:
        print('돈이 부족하여 돈을 돌려줍니다.')
    if coffee == 0:
        print('품절되었습니다. 판매를 중지합니다.')
        break
                                        
