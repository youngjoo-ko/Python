'''
## 모듈과 패키지(모듈<패키지)
* 모듈 : 함수, 클래스를 모아놓은 파일
* 패키지(폴더): 비슷한 기능(모듈, 함수, 클래스 등)들을 모아놓은 공간
 - A.A_1.aaa = A 패키지 안의 A_1 서브패키지 안의 aaa 모듈 호출
 '''

 # 상대 경로
# ../ : 부모 디렉토리 
# ./ : 현재 디렉토리

# 사용예1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(3)
Fibonacci().title

# 사용예2(클래스)
from pkg.fibonacci import *  # 권장하지 않음

# 사용예3(클래스)

from pkg.fibonacci import Fibonacci as fb

# 사용예4(함수)
import pkg.calc as c
print(c.add(10, 10))

# 사용예5(함수)
from pkg.calc import div as d
print(d(100,10))

# 사용예6
import pkg.print as p
p.prt1()
p.prt2()

import pkg.greet