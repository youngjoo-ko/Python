# 자료형 연습문제 

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print(len(q1))


# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print('apple;orange;banana;lemon')


# 3. 화면에 * 기호 100개를 표시하세요.

print('*'*100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

print(int("30"))
print(float("30"))
print(complex("30"))
print(str("30"))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

a = "Niceman"
print(a[4:])
print("Niceman"[4:])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
a = "Strawberry"
print(list(reversed(a)))

print(a[::-1])

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

p_number = "010-7777-9999"
print(p_number.split('-'))
print(type(p_number))

# 정규 표현식(Regular Expression)
import re
print(re.sub('[^0-9]','',p_number))


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

url = "http://daum.net"
print(url[7:])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

print("NiceMan".upper())
print("NiceMan".lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

c = "abcdefghijklmn"
print(c[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

p = ["Banana", "Apple", "Orange"]
del p[1]
print(p)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

li = list((1,2,3,4))
print(li)


print([s for s in li])

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

dic = {'성인' : 100000 , '청소년' : 70000, '아동' : 30000}
print(dic)

dic = {}
dic['성인'] = 100000
dic['청소년'] = 70000
dic['아동'] = 30000
print(dic)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

dic['소아'] = 0
print(dic)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print(dic.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.

print(dic.values())

# *** 결과 값만 정확하게 출력되면 됩니다. ^^
