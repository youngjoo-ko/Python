#문제1. while문을 이용하여 구구단을 위와 같이 출력하라
i = 2
while i <= 9:
    j = 1
    while j <= 9: 
        print('{0} * {1} = {1}'.format(i,j,i*j))
        j += 1
    i += 1

#문제2. 1~100까지 정수 중 2의 배수 또는 11의 배수를 모두 출력하라
print(list(range(2,101,2)) + list(range(11,101,11)))

num = list(range(1,101))
z = []
for i in num:
    if i % 2 == 0 or i % 11 == 0:
        z.append(i)                
print(z)


j = [i for i in range(1,101) if i % 2 == 0 or i % 11 == 0]
print(j)

# z = []
# z.append(i)   
# print(z)
# 결과값 하나씩을 리스트에 추가하고 싶은데 모르겠다
# 나는 마지막에 리스트를 만들고 추가했었는데 안됐었다, 방법은 리스트를 for 반복문 전에 만드는 것 
# for 다음이나 if 다음에 만들면 오류가 난다

# 문제3. a = [22,1,3,4,7,95,21,55,87,99,19,20,45]에서 최대값과 최소값을 찾으시오(sort, sorted 사용금지)

a = [22,1,3,4,7,95,21,55,87,99,19,20,45]
_min = a[0]
_max = a[0]
for x in a:
    if x < _min:
        _min = x
    if x > _max:
        _max = x
print(_min, _max)



_min = a[0]
_max = a[0]
for x in a[1:]: # 첫번째 요소를 비교할 필요가 없기 때문
    if x < _min:
        _min = x
    if x > _max:
        _max = x
print(_min, _max)


a.sort()
print(a[0], a[-1])

# 문제 4. a = [22,1,3,4,7,95,21,55,87,99,19,20,45]에서 평균을 구하시오

a = [22,1,3,4,7,95,21,55,87,99,19,20,45]

print('%.2f' %(sum(a)/len(a)))

i = 0
_sum = 0
while i < len(a):
    _sum += a[i]
    i += 1
print(_sum/len(a))


# 위를 for문으로 변환하면
_sum = 0
for i in a:
    _sum += i
print(_sum/len(a))


