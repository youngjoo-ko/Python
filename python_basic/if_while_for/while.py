# 나무를 10번 찍으면 넘어가는 반복문 작성해보기
hit = 0 # 나무를 찍은 횟수
while hit < 10:
    hit = hit + 1
    print('나무를 %d번 찍었습니다.' %hit)
    if hit == 10:
        print('나무 넘어갑니다.')

prompt = """
1. add
2. del
3. list
4. quit
"""

number = 0 
while number != 4:
    print(prompt)
    number = int(input("숫자를 입력하세요: "))