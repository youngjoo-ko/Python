'''
for 문
리스트, 문자열 등 순회 가능한 객체를 순회하면서 값을 처리할 때 사용
모든 아이템이 순회되면 블록 종료
'''



# 숫자는 순회불가능한(not iterable) 객체이기 때문에 에러
# iterable 객체 : 리스트, 튜플, 집합, 사전, 문자열


a = 'hello world'
for ch in a:
    print(ch)

a = [1, 10, 3, 4, 5]

for num in a:
    if num % 2 == 0:
        print(num/2)
    else:
        print(num+1)
    print(num)

'''
dict의 아이템 출력하기
dictionary의 경우 순회하게 되면 기본적으로 key값을 참조
keys()함수를 이용하여 key값만 순회 가능
values()함수를 이용하여 value값만 순회 가능
items()함수를 이용하여 tuple 형태로 key, value 순회 가능
'''

a = {'Korea' : 'Seoul', 'Japan' : 'Tokyo', 'Canada' : 'Ottawa'}
for k in a:
    print(k)

for key in a.keys():
    print(key)

for value in a.values():
    print(value)

for i in a.items():
    print(i)

li = list(a.items())
print(li)

for key, value in li:
    print(key, value)

'''
for에서 index 사용하기
기본적으로 for에 리스트를 순회하는 경우, 값만 추출함
iterable 객체를 리턴하는 함수
range(), reversed(), enumerate(), map() 등

'''

a = ['가','나','다','라','마']
for index, num in enumerate(a):
    if index >= 0: 
        print(index, num)


'''
range 함수
리스트를 쉽게 만들 수 있는 내장함수
주어진 값에 따라 다양한 결과를 반환
'''

a = list(range(1,201))
print(a)

print(list(range(1,101,5)))

# range함수 사용하여 1부터 100사이의 5의 배수만을 갖는 리스트를 생성하시오
c = list(range(5,101,5))
print(c)

for v in range(10):
    print(v)

for v in range(1,11,2):
    print(v)

# 1~100까지의 합을 range()함수를 이용해 출력하라

print(sum(range(1,101)))

#1~100 안에서 3의 배수의 합을 range()함수를 이용해 출력하라
# li = list(range(3,101,3))
# print(li)
# print(sum(li))

print(sum(range(3,101,3)))

############## for문 연습 ############
names = ['Kim', 'Park', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are ', name)

word = 'dreams'
for s in word:
    print('word: ', s)

# 소문자를 대문자로 출력
greeting = 'GoodMornig'
for g in greeting:
    if g.isupper():
        print(g)
    else:
        print(g.upper())

# 소문자를 대문자로 대문자를 소문자로 바꾸기
greeting = 'GoodMornig'
for g in greeting:
    if g.isupper():
        print(g.lower())
    else:
        print(g.upper())


# for - else 실습
# 반복문이 끝까지 수행된 경우 마지막 else 블럭을 수행
# members = [14,3,4,5,10,24,37,15,36,38]
members = [14,3,4,5,10,24,33,15,36,38]

for num in members:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found: ", num)
else:
    print("Not found...")


'''
for(loop)중첩
중첩의 개수는 무제한이다
반복횟수는 외부루프 x 내부루프
'''

a = [1,2,4]
for i in a:    # 외부루프가 1바퀴 돌 때 내부루프는 3바퀴돈다
    for j in a:
        print(i*j)

# 구구단 출력
x = [2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]
for i in x:
    for j in y:
        print(i, '*', j, '=', i*j)



