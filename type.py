# 파이썬의 데이터 타입(자료형)
# 숫자형, 숫자형 연산
'''
int: 정수
float: 실수
complex: 복소수
bool: 불린
str : 문자열

list : 리스트
tuple: 튜플
set: 집합
dict: 사전
'''

# 데이터 타입 연습
v_str1 = "Good Man"
v_bool = True
v_str2 = "Good Night"
v_float = 10.0
v_int = 7
v_list = [v_str1,v_str2]
v_dict = {
    "name" : "홍길동",
    "age" : 28
}
v_tuple = 3, 6, 8
v_set = {7, 8, 9}

# 데이터타입 출력
print(type(v_str1))
print(type(v_str2))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print(type(v_list))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))

'''
<변수 이름 규칙>

숫자로 시작하는 변수 이름은 X
일반적으로 소문자로 만든다 
예약어는 변수로 사용 X

<숫자형 연산자>
+, -, *, /, %(나머지연산자, mod), //(몫을 정수로 표현)
abs(변수): 절대값
pow(a,b) : a의 b승
x**y : x의 y승

'''

print(10//2)
print(10/2)


# 정수 선언
i=77
ii=-21
print(ii)
big_int = 55555555555555555555555
print(big_int)

# 실수 선언
f = 0.21
f2 = 3.555
f3 = 9/3

print(f3)

print("+++++++++++++++++++++")
print("i + ii:", i + ii)
print("f + f2:", f + f2)
print("i + f2:", i + f2)


a=3
b=2
print(a**b)

# 형 변환(casting)
# int, float
a = 5.
b = 4
c = 10

result = a+b
print(result)
print(int(result))
print(float(c))
print(complex(3))

print(int(True))
print(int(False))

print(int('3'))

# 수치연산 함수
print(abs(-7))
n,m=100,200
n,m=divmod(100,8)
print(n,m)

import math
#  ceil(), floor()
print(math.ceil(5.3))
print(math.floor(3.8))
print(round(4.7))