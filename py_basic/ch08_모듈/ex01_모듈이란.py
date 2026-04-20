# 모듈(module)이란?
# 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다

# 모듈 만들기
# mod1.py

# 모듈 불러오기
# import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
# 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.
# C:\Users\pc07-00\AppData\Local\Programs\Python\Python313\Lib 

# import 모듈_이름 (확장자 제외)
# import mod1

# 모듈에 있는 함수 사용하기
# print(mod1.add(3, 4)) #7
# print(mod1.sub(4, 2)) #2

# from 모듈_이름 import 모듈_함수
from mod1 import add, sub
print(add(3, 4)) #7
print(sub(4, 2)) #2

from mod1 import * #많으면 "*"로 표기할 수 있다.


# if __name__==__main__





