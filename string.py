### 문자열 생성
str1 = "I am boy"
str2 = 'Good Man'

print(str1)

#### 문자열 길이
# len()함수는 문자열의 길이를 반환

print(len(str1))

str4 = ''
str5 = str()

print(len(str4))
print(len(str5))


#### 이스케이프 문자 사용방법
e_str1 = "Do you have a \"big collection\"?"
print(e_str1)
e_str2 = 'What\'s on TV?'
print(e_str2)
e_str3 = 'This is a "book"'
print(e_str3)

# 탭, 줄바꿈
t_s1 = "Tab\tClick"
print(t_s1)
t_s2 = "New line\n Start"
print(t_s2)

#### Raw String
# c:\Programs\python\ 출력해보기
a = 'c:\\Programs\\python\\'
print(a)

r_s1 = r'c:\Programs\python\''
print(r_s1)

r_s2 = r"\\a\b\c\d"
print(r_s2)

r_s3 = r"\'"
print(r_s3)

#  멀티 라인 출력
multi_str1 = \
"""
문자열
멀티라인
테스트
"""
print(multi_str1)

###  문자열 연산
_str1 = '*'
_str2 = 'abc'
_str3 = 'def'
_str4 = 'Kim Lee Park Jung'

print(_str1 * 100)
print(_str2 + _str3)
print(_str1 * 3)
# print(_str4 + 5) 타입 불일치로 에러

print('x' in _str4)
#  _str4 안에 x가 없기 때문에 False

print('P' in _str4) 
# 대소문자 구별한다

print('P' not in _str4)

### 문자열 형 변환
print(type(str(77)))  # str => string을 의미
print(type(str(10.4)))  # 실수형을 문자형으로 변환
print(str(True))

### 문자열 함수
a = 'Goodman'
b = 'orange'

print(a.islower()) # 소문자냐 묻는 함수
print(a.isupper()) # 대문자냐 묻는 함수
print(a.endswith('e')) # e로 끝나냐고 묻는 함수
print(a.capitalize()) # 첫 글자만 대문자로
print(a.replace('good', 'nice')) #good 을 nice로 대체
print(list(reversed(b))) # list를 사용해 역순으로 출력

aa = 'hello world'
print(aa.upper())
# split() : 문자열 중 포함된 특정한 문자로 구분하여 문자열의 리스트로 리턴
cc = 'hello world what a nice weather'
print(cc.split('w'))

dd = '2020-07-15'
print(dd.split('-'))

'''
### ***슬라이싱(아주중요)
 - 문자열의 각 문자는 순서가 있음
 - 이 때, 각 문자열의 순서를 **인덱스**라고 함
 - 첫 번째 문자부터 마지막까지 차례대로의 순서를 갖는다(0부터 시작)
 '''

str11 = 'NiceBoy'
print(str11[0:3])
print(str11[:len(str11)])
print(str11[:len(str11)-1])
print(str11[:])# 처음부터 끝까지

str22 = 'orange'
print(str22[1:4])
print(str22[1:4:2])
print(str22[1:-2])
print(str22[::-1])
print(str22[::1])
print(str22[::-2])
print(str22[::])

# 문자열은 immutable 객체이다
a = 'hello world'
print(a)
print('y' + a[1:])

print(a.replace('h', 'y'))

z = 32.444
print("{0:10.2f}".format(z))
print('%10.2f' %32.444)