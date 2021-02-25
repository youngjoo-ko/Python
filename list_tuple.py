'''
### 리스트&튜플
- 복수개의 값을 담을 수 있는 데이터 구조
- 실생활에서 사용하는 리스트(학생, 성적 등)과  동일한 의미로 이해
- list : mutable(생성된 후에 변경 가능)
- tuple : immutable(생성된 후에 변경 불가능)


#### <리스트 초기화 방법>
- []안에 값을 담아서 생성
- list()함수로 생성
- str.split()함수로 생성

#### <리스트 자료형의 특징>
- 순서가 있다
- 중복 허용
- 수정 가능
- 삭제 가능

#### <튜플 자료형의 특징>
- 순서가 있다
- 중복 허용
- 수정 불가
- 삭제 불가
'''

# 선언
# name1 = '아무개'
# name2 = '홍길동'
a = []
print(a)
b = list() # 명시적 선언
c = [1,2,3,4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange' ]]

print(c[2])
print(c[-2])
print(d[3])
# e에서 두가지 방법으로 Banana를 출력해라
print()
#1 
a = e[2]
print(a[1])
#2
print(e[2][1])
print(e[2][-2:2])
print(e[2][-1:-2])

# e에서 슬라이싱기법으로 바나나와 오렌지를 꺼내라
print(a[1:3])
print(e[2][1:3])
print(e[2][-2:3])

a = '20200715sunny'
year = a[:4]
day = a[4:8]
weather = a[8:]

print(year + day + weather)
print(year, day, weather)
# 더하기연산은 붙여쓰기
# 컴마는 띄어쓰기

print('Today is', weather, 'day')
print('Today is', a[8:], 'day')

################ 리스트 연산 #############
print('c + d:', c + d)
print('c * 3:', c*3)
# print("'hello' + c[0] :", 'hello' + c[0]) 타입 불일치로 에러
print("'hello' + c[0] :", 'hello' + str(c[0]))

############## 리스트 수정, 삭제#############
c[0] = 77
print('c: ', c)

# 슬라이싱은 삽입이 발생
c[1:2]= ['a', 'b', 'c']
print('c: ', c)

# 리스트안에 리스트가 들어감
c[1] = ['a', 'b', 'c']
print('c: ', c)

# 삭제
c[1:3] = []
print('c: ', c)

#del을 이용한 삭제
del c[3]
print('c: ', c)

############ 리스트 함수##############
a = [5, 2, 1, 3, 4]
a.append(66)
print(a)

print("<정렬 함수>")
a.sort() # 오름차순 정렬
print('a: ', a)
a.reverse() #내림차순 정렬
print('a: ', a)

print("<인덱스 함수>")
print(a.index(5)) #5의 위치값(1번 인덱스에 위치)

print("<insert 함수>")
a.insert(2,7) # 2번 인덱스에 7을 삽입
print('a: ', a)

print("<remove 함수>")
a.remove(1) # 데이터 값을 찾아서 삭제(리스트 중 숫자 1을 삭제함)
print('a: ', a)

print("<pop 함수>")
a.pop() # 맨 마지막을 꺼내고 리스트에서 삭제시킴
print('a: ', a)

print("<count 함수>")
# 리스트 안 요소의 갯수 확인
print(a.count(4))

b = [1, 1, 4, 2 ,5, 100]
print(b.count(1))

print("<extend 함수>")
ex = [8,9]
b.extend(ex) # ex에 할당된 리스트의 요소값만 b에 확장시킴(확장시키는 요소는 반드시 리스트여야만 함)
print(b) 
b.append(ex) # ex에 할당된 리스트 자체를 b에 추가시킴
print(b) 

# 리스트 삭제 관련 함수 : del, remove, pop

############# 튜플 ##############
a = ()
b = (1,) # 튜플을 선언할 때는 반드시 컴마가 필요
c = (1,2,3,4)
d = (10, 100, ('a','b','c')) 

print("<인덱싱>")
print(d[2][1])

print("<슬라이싱>")
print(d[0:2])
print(d[2][1:3])

print("<튜플 연산>")
print('c+d: ', c + d)
# print('c+3: ', c + 3) 타입 불일치로 에러
print('c+3: ', c + (3,)) # 3을 튜플 타입으로 만들어 더한다
print("'hi' + c[0] : ", 'hi' + str(c[0])) # 인덱싱으로 가져온 값을 문자열 타입으로 만들어 더한다

print("<튜플 함수>")
a = (5, 4, 3, 2, 100, 100)
print(3 in a) # 3이 변수 a에 있냐고 물음
print(a.index(5))
print(a.count(100))