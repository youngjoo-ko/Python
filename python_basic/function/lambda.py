### lambda 함수의 이해
'''
* 단일문으로 표현되는 익명의 함수
* 익명 함수 : 이름이 없고, 구현체만 존재하는 간단한 함수
* 코드 상에서 한번만 사용되는 기능이 필요할 때, 일회성(단발성)으로 만들어 사용한다(함수 만들기는 복잡하므로)
* 메모리가 필요없다
'''

def square(x):
    return x**2

square(10)

sq = lambda x: x**2 # lambda 뒤에 있는 것은 매개변수, 콜론뒤에 있는건 결과값
print(type(sq)) # 람다함수를 변수에 넣으면 해당 변수는 함수 객체가 된다
sq(10)

la = lambda x, y: x+y
la(5,6)

def str_len(s):
    return len(s)

str_len('goods')

strg = ['bob', 'charles', 'alex', 'teddy']
# strg.sort() # 알파벳 순으로 정렬
strg.sort(key=str_len)
print(strg)

# lambda 함수를 사용하는 이유: 위 처럼 str_len 함수 정의가 필요없기 때문
# 메모리를 차지하지 않기 때문에 효율적
strg.sort(key = lambda s: len(s))
print(strg)

'''
### filter, map, reduce 함수
* lambda가 유용하게 사용되는 대표적인 함수 3가지
* 함수형 프로그래밍의 기본요소
* fiter :  특정 조건을 만족하는 요소만 남겨두고 필터링해줌
* map : 각 원소를 주어진 수식에 따라 변형하여 새로운 리스트를 반환해줌
* reduce : 앞 2개의 원소를 순서대로 연산 후 그 연산의 결과가 또 다음 연산의 입력으로 진행됨. 따라서, 마지막까지 진행되면 최종출력은 한개의 값만 남게된다
'''

def even(a):
    return a % 2 == 0

even(10)

# fiter(함수, 리스트)

nums = [1,2,3,6,8,9,10,11,13,15]

# 리스트의 각 원소를 even 함수에 적용하여 짝수만 필터링 한것 
# 즉, true 값만 포함하고 나머지는 버림
list(filter(even, nums))

list(filter(lambda x: x % 2 == 0, nums))

# map(함수, 리스트)
# 주어진 리스트의 제곱값을 리스트로 표현하라
nums = [1,2,3,6,8,9,10,11,13,15]
b = list(map(lambda y: y**2, nums))
print(b)

nums = [1,2,3,6,8,9,10,11,13,15]
b = list(map(lambda y: y % 2 == 0, nums))
print(b)

# reduce(함수, 리스트)
# functools 모듈에 있는 함수
# 왼쪽에서 오른쪽으로 반복하면서 함수 연산을 한다
# 즉, 왼쪽에서 오른쪽으로 순회하면서 x는 왼쪽, y는 오른쪽에 할당된다

# 리스트 내의 모든 숫자를 합산 

import functools
a = [1, 3, 5, 8]
b = functools.reduce(lambda x, y: x + y, a)
print(b)

from functools import reduce  
a = [1, 3, 5, 8]
c = reduce(lambda x, y: x * y, a)
print(c)


# 숫자 초기값 고정하기
aa = reduce(lambda x,y: x + y, a, 100) # 100에 a의 총합을 더한 값이 반환된다
print(aa)

# 문자열 더하기
bb = ['1', '3', '5', '8']
cc = reduce(lambda x,y: x + y, bb)
print(cc)

# 문자열 초기값 고정하기
dd = reduce(lambda x,y: x + y, bb, 'str 더하기: ')
print(dd)

## sort(), sorted() 함수
# sort() : 기존 리스트의 정렬을 바꾼다
# 오름차순 정렬
li = [100, 11, 33, 47, 10]
li.sort()
print(li)

# 내림차순 정렬
li.sort(reverse = True)
print(li)

# sorted() : 기존 리스트는 그대로 두고, 정렬한 새로운 리스트를 만든다 
# sort()함수 보다 활용도와 사용빈도가 높다
li = [100, 11, 33, 47, 10]
a= sorted(li)
print(a)
print(li) # 기존 li는 그대로 남아있음

dic = {3:'A', 2:'C', 6:'F', 1:'D'}
sorted(dic) # 키 순으로 오름차순 정렬

member = [('강호동', 50, '제주'),('이경규', 58, '수원'),('유재석', 44, '인천')]
sorted(member) # 튜플에서 첫번째 요소인 이름 오름차순으로 정렬

# 위 멤버의 주소를 오름차순으로 정렬
a = list(sorted(member, key = lambda x: x[2]))
print(a)

# 나이를 오름차순으로 정렬
b = list(sorted(member, key = lambda y: y[1]))
print(b)

# 나이를 내림차순으로 정렬
b = list(sorted(member, key = lambda y: y[1], reverse=True))
print(b)

## 함수 연습문제

# 1. 주어진 숫자 리스트의 평균을 구하는 함수를 정의하여 출력하시오 
# (함수명 mean, 입력은 숫자리스트, 출력은 숫자리스트의 평균)

from functools import reduce 
bob = [30, 80, 90, 100]
b = reduce(lambda x,y: x + y, bob)/len(bob)
print(b)

def mean(score_list):
        return sum(score_list)/len(score_list)    
print(mean(bob))

# 2. 주어진 숫자가 소수인지 아닌지 판별하는 함수를 정의하여 출력하시오
# 입력: 양의 정수 1개, 출력: boolean


def is_p(a):
    b = 0
    for i in range(2,a):
        if a % i == 0:
            return False
    return True   

print(is_p(13))

#3.숫자 2~해당 숫자 사이에 소수가 몇개인지 출력하는 함수를 정의,출력
# 입력: 양의 정수 1개, 출력: 소수의 개수

def is_prime(n):
    cnt = 0
    for i in range(2,n+1):
        if is_p(i):
            cnt += 1
    return cnt

print(is_prime(7))
print(is_prime(10))
print(is_prime(13))
print(is_prime(100))