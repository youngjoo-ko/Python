'''
## 보조제어문(break, continue)
**break**
 - loop를 중단 시 사용
 - 보통 조건문안에서 수행, 조건을 만족하는 경우 loop를 탈출하기 위해 사용함
 - loop를 중단하는 경우, 'while 또는 for 이후'의 코드를 수행
'''

a = [11, 10, 9, 24, 555, 33, 44, 66, 88]

i = 0
while i < len(a):
    if a[i] > 20:
        break
    print(a[i])
    i += 1
print('End of while')



'''
continue
continue 다음 명령을 건너뛰고 다시 while, for 조건으로 점프함
특정한 경우에는 코드를 수행하지 않고 다음으로 건너뛰기 위해 사용
'''

a = 7
while a > 0:
    a -= 1
    if a == 5:
        continue
    print(a)