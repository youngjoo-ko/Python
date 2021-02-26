## 사용자로부터 입력을 받는 함수
yourname = input('당신의 이름을 입력하세요: ')

print('당신의 이름은 {} 입니다'.format(yourname))

yourage = input('당신의 나이를 입력하세요: ')
print('당신의 나이는 {} 입니다'.format(yourage))

yourname, yourage = input("당신의 이름과 나이를 입력하세요: [홍길동 20]").split(' ')
print('당신의 이름은 {}이고, 나이는 {}세 입니다'.format(yourname, yourage))

while True:
    try:
        yourname, yourage = input("당신의 이름과 나이를 입력하세요: [홍길동 20]").split(' ')
        print('당신의 이름은 {}이고, 나이는 {}세 입니다'.format(yourname, yourage))
        break
    except ValueError:
        print("이름과 나이를 띄어쓰기 하세요")

# 입력받은 단수의 구구단만 출력하는 코드
a = int(input('출력하고자 하는 구구단의 단수를 입력하세요: '))
for b in range(1,10):
    print("{} x {} = {}".format(a,b,a*b))


## f스트링
#python 3.6.x 부터 지원하는 문자열 포맷팅
# 변수를 {}에 넣어서 사용 가능
# 직관적이며 사용하기 편리

# f스트링 사용
a = int(input('출력하고자 하는 구구단의 단수를 입력하세요: '))
for b in range(1,10):
    print(f'{a} x {b} = {a*b}')

# 원하는 단수를 입력받아 구구단 출력하기
while True:
    s = int(input('출력하고자 하는 구구단의 시작 단수를 입력하세요: '))
    e = int(input('출력하고자 하는 구구단의 마지막 단수를 입력하세요: '))
    if s<e: break
    print("다시 입력하세요")
for n in range(s,e+1):
    print(f'-------{n}단-------')
    for m in range(1,10):
        print(f'{n} x {m} = {n*m}')

# 구구단 가로 출력하기
for n in range(1,10):
    for m in range(2,10):
        print(f'{m} x {n} = {m*n}', end='\t')
    print()

## 문제풀기
# 메뉴1 함수로 정의   
def menu_1():
    a = int(input('출력하고자 하는 구구단의 단수를 입력하세요: '))
    for b in range(1,10):
        print(f'{a} x {b} = {a*b}')

# 메뉴2 함수로 정의   
def menu_2():
    for n in range(2,10):
        print(f'-------{n}단-------')
        for m in range(1,10):
            print(f'{n} x {m} = {n*m}')

# 메뉴3 함수로 정의   
def menu_3():
    for x in range(1,10):
        for y in range(2,10):
            print(f'{x} x {y} = {x*y}', end='\t')
        print()


option = '''
<---------메뉴--------->
[1]. 원하는 단 출력하기
[2]. 구구단 세로 출력하기
[3]. 구구단 가로 출력하기
[4]. 종료하기
<--------------------->
'''


while True:
    print(option)
    a = int(input('원하는 메뉴를 선택하세요: '))
    if a == 1:
        menu_1()
    elif a == 2:
        menu_2()
    elif a == 3:
        menu_3()
    elif a == 4:
        print()
        print("---------------프로그램이 종료되었습니다---------------")
        break
    else:
        print()
        print("!!!입력오류!!! 1~4까지 숫자를 입력하세요")
