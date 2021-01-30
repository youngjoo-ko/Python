'''
# 조건문 정리
* 파이썬에서는 모든 블록{}의 시작점의 마지막에는 :(콜론)을 쓴다
* 조건문의 경우 if, elif, else 블록에 종속된 코드는 들여쓰기 해야한다
  - 들여쓰기가 된 코드를 블록(block), 또는 코드블록 라고 함
'''



if 6>=5:
    print('6은 5보다 크다')
    print('맞아!!!')
print('이 코드는 if문에 종속된 코드가 아니다')


# bool 자료형을 많이 활용한다
print(type(True))
print(type(False))


# 조건문 기본 형식
if True:
    print("Yes") # 콜론, 들여쓰기(indent) 주의!!!!
if False:
    print("No")
    
if False:
    print('You can\'t reach here') # 끝에 큰 따옴표를 써줘도 됨
else:
    print('Oh, you are here')


# 관계(비교) 연산자
# > , >=, <, <=, ==, !=

a = 10
b = 0

# a와 b가 같을 때
print(a == b)
print(a!=b)


### 참, 거짓의 종류(중요!!!!!!)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0, None
# 조건이 참 일때 명령문이 출력된다

city = ''
if city:
    print('you are in:', city)
else:
    print('Please enter your city')
    
city = 'Incheon'
if city :
    print('You are in:', city)
else:
    print('Please enter your city')



############ 논리 연산자 : and, or not ############
a = 10
b = 8
c = 11
# if a == 10 and b == 9:  # 조건이 거짓이므로 다음 명령문이 출력되지 않음
if a == 10 or b == 9: # b == 9와 상관없이 무조건 참
    print('That is True')
    
if a == 10 or b == 9 and c == 12: # 우선순위 : and가 or 보다 우선
    print('That is True')
    
if (a == 10 or b == 9) and c == 12: # or을 먼저 연산하고 싶으면 ()를 쓴다
    print('That is True')
    
if not a == 10:  # not True 이므로 결과가 출력되지 않음
    print('a is ten')
    
if 3: # 0이 아닌 숫자는 참
    print('333333')
    
aa = 0
if aa:
    print('print')


# if else
a = 9
if a % 2 == 0: # 짝수인지 판별
    print(a/2)  # if와 else사이에 다른 명령이 들어가면 오류 발생
else:
    print(a+1) 
    
# if elif else
bb = 16
if bb % 4 == 0:
    print('bb는 4의 배수')
elif bb % 4 == 1:
    print('bb % 4 is 1')
elif bb % 4 == 2:
    print('bb % 4 is 2')
else:
    print('bb % 4 is 3')


a = 7

if a % 4 == 0:
    print('bb는 4의 배수')
if a % 4 == 1:
    print('bb % 4 is 1')
if a % 4 == 2:
    print('bb % 4 is 2')
if a % 4 == 3:
    print('bb % 4 is 3')


# 중첩 조건문(nested condition)
#- 중첩의 의미는 depth(깊이)로 생각하면 됨. depth의 제한은 없음

a, b, c = 10, 9, 8

if a == 10:
    if c == 8:
        if b == 8:
            print('a is ten and b is 8')
        else:
            print('a is ten and b is not 8')

pocket = ['water', 'card', 'phone']
if 'card' in pocket:
    print('버스를 타고가라')
else:
    print('걸어가라')

pocket = ['water', 'card', 'phone']
if 'money' in pocket:
    print('버스를 타고가라')
elif 'card' in pocket:
    print('버스를 타고가라')
else:
    print('걸어가라')

pocket = ['water', 'card', 'phone']
if 'money' in pocket: pass
else: print('카드를 꺼내라')

score = 100
if score>=60:
    message = 'success'
else:
    message = 'failure'
print(message)

# if의 조건부 표현식(활용성 ,가독성 높음)
message = 'success' if score>=60 else 'failure'
print(message)