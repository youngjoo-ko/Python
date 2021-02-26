# 함수
'''
* 그 동안 우리는 무심코 많은 함수를 사용했음
 - print(), sum(), range() 등등
 - 주어진 입력(input)에 대해서 의도한 대로 출력(output)함
 - 위의 함수들은 모두 파이썬의 내장함수(built-in function)
 '''

a = [1,2,3,4]
length = len(a)
print(length)

total =sum(a)
print(total)

## 함수의 정의(사용자 정의함수)
'''
* 정의 시 def 라는 키워드를 사용
* 인수, 인자, 매개변수(argument 또는 parameter)를 정의해야 함
* 콜론 필요
* 함수의 구현부분은 블록(body)이다
 - 블록 내부에는 return 키워드를 사용해 출력값을 전달한다
* 함수명 설정 방법
 - 어떤 기능을 하는 함수인지 이름으로 최대한 표현하는 것이 좋다



*함수의 호출*
함수명()

주의점: 함수 선언의 위치는 함수호출 보다 먼저 선언되어야 한다
'''

def add(x,y):
    n = x + y
    return n

c = add(100, 10) # 정의한 함수의 매개변수 개수와 동일하게 입력해야 함
print(c)

def say():
    print("hello world") # 리턴값이 없을 수도 있다

say()

'''
### parameter: 매개변수
* 함수를 정의할 때 전달되는 입력값(input)을 받는 변수 add(x,y)
 - 입력이 필요하지 않은 함수도 있다
* 어떠한 타입의 객체도 올 수 있다(함수도 가능)
* 기본적으로 함수에 정의된 인자 순서에 따라 값을 전달한다 add(x,y) = add(100,10)


### argument: 인수
* 함수를 호출할 때 전달하는 입력값을 의미 add(100,10)

### Default parameter(기본값)
* 함수를 정의할 때 인수의 기본값 지정 가능
 - 호출한 함수에서 인수를 입력하지 않은 경우, 지정된 기본값으로 대체된다
 
### Default parameter 사용시 주의점
* 기본값 뒤에 일반 매개변수가 위치할 수 없음
> def test(a, b=1, c) 사용x
> def test(a=1, b, c) 사용x
'''

def add(x, y=5, z=5): # 매개변수의 기본값 지정
    a = x + y + z
    return a

print(add(10, 20, 30))
print(add(10,20))

# 기본값의 다른 예 : print함수
# print 함수는 sep, endm file 등의 여러 기본인자를 갖고있다

print(1,3,5)
print(1,3,5, sep='!')
print(1,3,5, end = '^^') # end기본값은 줄바꿈 
print(100)


### keyword parameter
'''
* 인수에 값을 전달할 때, 이름을 명시하여 전달 가능(순서를 바꾸는 것도 가능)
 - 이름을 사용하지 않은 경우, 기본적으로 순서에 맞게 전달
 '''
def test(x, y, z):
    a = x + y + z
    return a
test(x=10, y=5, z=10)
test(y=8, z=10, x=9)

### return(결과값, 전달값)
'''
* 함수의 종료를 명시
 - return 옆에 값이나 수식이 있는 경우, 해당 값 or 수식을 호출자(caller)에게 전달(반환)하고 종료
 - return이 없거나 함수 조건에 맞지 않는 경우, 함수 코드블록이 종료된 것으로 간주하여 None을 반환
'''

def aa_mu1(x, y):
    if x > 10:
        return x * y
        return
    print(x + y)
    return (x + 2)*y
    print(x + y) # 이 구문 전에 이미 return값이 출력됐으므로 해당 구문은 출력되지 않는다
    
# c = aa_mu1(3,5) # 인자가 10보다 작으므로 결과값이 출력되지 않는다
c = aa_mu1(11,5)
print(c)


def aa_mu2(x, y):
    if x > 10:
        return x * y

c = aa_mu2(3,5)
print(c)

# 다중리턴
def add_mul(x,y):
    s = x + y
    m = x * y
    n = x * 100
    
    return s, m, n

c = add_mul(20,3)
print(c)

cc,dd,nn= add_mul(20,3)
print(cc,dd,nn)

# 튜플 리턴
def b_func(x):
    y1 = x*2
    y2 = x*4
    y3 = x*6
    return(y1,y2,y3)
tup = b_func(4)
print(type(tup),tup,list(tup))

# 리스트 리턴
def a_func(x):
    y1 = x*2
    y2 = x*4
    y3 = x*6
    return[y1,y2,y3]
c = a_func(4)
print(type(c),c,set(c))

# 딕셔너리 리턴
def d_func(x):
    y1 = x*2
    y2 = x*4
    y3 = x*6
    return{'r1': y1, 'r2': y2, 'r3': y3}
dic = d_func(8)
print(dic)

'''
### 변수의 범위(variable scope)
* 변수가 참조 가능한 코드상의 범위를 명시
* **지역변수(local variable)** : 자신이 속한 코드 블록이 종료되면 소멸되는 변수
* **전역변수(global variable)** : 가장 상단에서 정의되어 프로그램 종료 전까지 유지되는 변수
* 같은 이름의 지역변수와 전역변수가 존재할 경우, 지역변수의 우선순위가 높으므로 이 값이 선언이된다
'''

num1 = 10
num2 = 30

def test(num1, num2):
    print(num1, num2)
    return num1 + num2

print(test(100,200)) # 같은 이름이라도 우선순위에 있는 지역변수가 사용되었음
print(num1, num2) # 블럭을 나왔기때문에 전역변수 사용

print(num1, num2)

'''
### 가변길이 인자(Variable length argument)
* 전달되는 파라미터의 개수가 고정적이지 않은 경우 사용
 - print(), format()
> *args, **kwargs
'''

# 파라미터의 개수가 정해지지 않았기 때문에 얼마든지 넣을 수 있다
print()
print(1)
print(1,2,4)

def test(*x):
    print(type(x))
    
test()
test(10)
test(10,20)
test(10,20,30)

print('-----------------------------')
def test(*args): # 가변길이 함수는 관례적으로 args를 사용
    for item in args:
        print(item)
test(1,2,3,4,5,6)

def test2(**x):
    print(type(x))
    
test2(f=6)
test2(a=1, b=2, c=3, d=4, name = 'ko')
print('----------------------------------------')

def test3(**kwargs): # keyword arguments
    for key, value in kwargs.items():
        print('key:', key, 'value:', value)
test3(a=1)
test3(b=6, c=8, d=10)

_str = '오늘 온도: {}도, 강수확률: {}%'.format(20,60)
print(_str)