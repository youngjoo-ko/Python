'''

<딕셔너리 자료형(mutable)>
순서가 없다
중복 허용x
수정 가능
삭제 가능
딕셔너리는 JSON과 비슷
원소를 KEY와 VALUE의 한쌍으로 표현한다

'''

# 선언
#키는 중복불가 및 불변, 값은 중복가능 및 가변 
a = {'name':'Lee','Phone':'010-1234-1234','birth':'991010'}
b = {0: 'Hello Python!', 1:'Hello Coding',1:'Hello'}
b1 = {0: 'Hello Python!', 1:'Hello Coding',2:'Hello Coding'}
print('a: ',type(a), a)
print('b: ',type(b), b)
print('b1: ',type(b1), b1)

c = {'arr':[1,2,3,4]}
print('c: ',type(c), c)

####################################################
print(a['name'])
# print(a['age']) #데이터 없을 경우 에러
print(a.get('age')) #데이터가 없는 경우 None으로 출력, 안전하다
print(b[0])
print(b.get(0))
print(c['arr'][2])

######################################################
# 딕셔너리에 데이터 추가
a['age'] = 30
print(a)
a['addr'] = '인천'
print(a)
a['rank'] = (1,2,3)
print(a)

#################################################
# keys, values, items
print(a.keys())
print(list(a.keys())[3]) # 대괄호 위치 유의!!

#################################################
# keys
temp = list(a.keys())
print(temp)
print(temp[1:3])

###################################################
# values
print(a.values())
print(list(a.values()))
temp_v = list(a.values())
print(temp_v[1:5])

################################################
# items
print(a.items())
print(list(a.items()))
print(tuple(a.items()))

###########################################
print('name' in a)
print('name' in b)
