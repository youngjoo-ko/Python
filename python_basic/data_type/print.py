#  기본출력

print('hello python')
print("hello python")
print()
print('''hello python''')
print("""hello python""")

# separator 옵션
print('T', 'E', 'S', 'T', sep='/')

# SEP을 이용한 TEST 출력
print('T', 'E', 'S', 'T', sep='')

# 2020-07-14
print('2020', '07', '14', sep='-')

# test@naver.com 출력
print('test', 'naver.com',  sep='@')

print('-------------end 옵션---------------------')


# end 옵션의 default 값은 \n(개행)
print('welcome To', end='')
print('Test')


# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1}'.format('You', 'Me'))
print('{var1} and {var2}'.format(var1='You', var2='Me'))

# %d, %f, %s
print("%s의 나이는 %d" %('홍길동', int(33)))
print('test1: %5d, price: %10.2f' %(766,43.123))

'''
Escape 코드
\n: 개행 
\t: 탭
\\: \
\': '

'''

print('국어 \t 영어\t 수학')