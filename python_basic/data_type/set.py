
'''
### 집합(set) 자료형
- 순서가 없다
- 중복 허용x
- 수정, 삭제o(mutable 객체)
'''

# 선언
a = set()
print(a)
b = set('Good Morning')
print(b)
c = set([1,2,3,4])
print(c)
d = set([1,2, 'Pen', 'Korea', 'English'])
print(d)
e = set([1,1,3,3,4,5,6]) 
print(e) # 중복 허용하지 않기 때문에

# d를 튜플로 변환
d1 = tuple(d)
print(d1)
# d에서 Korea, Pen 추출하기
print((d1[2],d1[4]))

# d를 list로 변환
d2 = list(d)
print(d2)
print(d2[0], d2[1:3])

# set의 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2) # 교집합
print(s1.intersection(s2))

print(s1 | s2) # 합집합
print(s1.union(s2))

print(s1 - s2) # 차집합, 부분집합
print(s1.difference(s2))

# 데이터 추가 & 제거
ss1 = set([1,2,3,4])
ss1.add(55)
print(ss1)

ss1.remove(2)
print(ss1)