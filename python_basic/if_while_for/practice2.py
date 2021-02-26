# 제어문 연습문제

# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print(q1["가을"]) # 내가 한것

for k in q1.keys():
    if k == "가을":
        print(q1[k])

for k,v in q1.items():
    if k == "가을":
        print(v)


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# 아래는 내가 푼 정답, 이런 경우 key에 사과가 있는지 알 수 없다
if "사과" in q2.values():
    print("사과가 포함되어 있습니다")
else:
    print("포함되어 있지 않습니다")


# 따라서 아래와 같이 수행해주는 것이 좋으며, 이 경우 else블록의 들여쓰기를 주의하자!!!!
for k, v in q2.items():
    if v == '사과':
        print("사과가 포함되어 있습니다")
        break
else:
    print("사과가 포함되어 있지 않습니다")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.(점수는 임의로 지정하여 테스트)
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = [55, 25, 18, 90, 70]
num = 0

for score in score:
    num += 1
    if score <= 20:
        print("%d번 학생 E학점입니다" %num)
    elif score <= 40:
        print("%d번 학생 D학점입니다" %num)
    elif score <= 60:
        print("%d번 학생 C학점입니다" %num)
    elif score <= 80:
        print("%d번 학생 B학점입니다" %num)
    else:
        print("%d번 학생 A학점입니다" %num)

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = [12, 6, 18]
max1 = a[1]
for num in a:
    if num > max1:
        max1 = num
print(max1)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'

# 내가 푼 정답
if s[7] == '1' or s[7] == '3':
    print("남자")
if s[7] == '2' or s[7] == '4':
    print("여자")

# 다음처럼 더 간략하게 가능 
if s[7] == '1' or s[7] == '3':
    print("남자")
else: print("여자")

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
q3 = ["갑", "을", "병", "정"]

# 내가 푼 정답
del q3[3]
print(q3)

q4 = [s for s in q3 if s != "정"]
print(q4)

# 다른방법
s = []
for v in q3:
    if v == '정':
        continue
    else:
        s.append(v)
print(s)   # **********들여쓰기 주의**********


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)

print(list(range(1,101,2)))

z = []
for a in range(1,101):
    if a % 2 == 1:
        z.append(a)
print(z)


z2 = [a for a in range(1,101) if a % 2 == 1]
print(z2)


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

# 내가 푼
q5 = [word for word in q4 if len(word) >= 5]
print(q5)

# 다른방법
for v in q4:
    if len(v) >= 5:
        print(v)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

# 내가 푼 방법
q6 = [b for b in q5 if b.islower() == True]
print(q6)

# 다른방법
for b in q5:
    if b.islower():
        print(b, end=' ')

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

#내가 푼 방법
for x in q6:
    if x.isupper():
        print(x.lower())
    else:
        print(x.upper())


# 교수님
print([y.lower() if y.isupper() else y.upper() for y in q6])







