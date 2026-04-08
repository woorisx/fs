# 문자열 내장함수
# count('문자열'): 문자열의 개수
a = "hobby"
print(a.count('b')) # 2, 갯수 셀때


# find('문자열'): 문자열의 위치
a = "Python is the best of best choice"
print(a.find('b')) # 14, 몇번째인지(위치 알려줌) 왼쪽에서 오른쪽으로 찾음
print(a.find('k')) # -1, 없으면 -1을 출력한다.

# index('문자열')  문자열의 위치(왼쪽에서 오른쪽)
a = 'Life is too short'
print(a.index('t')) # 8
# print(a.index('k')) # 없으면 에러 

# join(B) : 하나씩 나누어서 ,로 구분 , B에 A를 삽입
print(",".join('abcd')) # a,b,c,d


# upper() : 대문자로
a = "hi"
print(a.upper())
# lower() : 소문자로
print(a.lower())

# 공백제거
a = '   hello world   '
# lstrip() : 왼쪽 공백 제거
ls = a.lstrip()
print(ls)
print(len(ls))

# rstrip() : 오른쪽 공백 제거
rs = a.rstrip()
print(rs)
print(len(rs))

# strip() : 공백 제거
ss = a.strip()
print(ss)
print(len(ss))

# replace(문자열, 새로 바꿀 문자열) 변경
a = "Life is too Short"
print(a.replace("Life", "Your Leg"))
print(a.replace("Short", "long"))


# split(["구분자"]) 
# 구분자 기본값은 공백이며, 리스트로 출력된다.
a = "Life is too Short"
print(a.split()) # ['Life', 'is', 'too', 'Short'] -> 리스트
b = "a, b, c, d"
print(a.split(","))


# 논리값 출력 함수
# is***() true 또는 false로 반환
# isAlpha() 숫자인지 문자인지 구분
a = "Python"
print(a.isalpha()) # True
a = "Python3"
print(a.isalpha()) # False
a = "Hello Python!"
print(a.isalpha()) # False : 느낌표때문에

# isdigit()
a = "12345"
print(a.isdigit()) # True
a = "12삼45"
print(a.isdigit()) # False
a = "12 45"
print(a.isdigit()) # False 공백때문에
a = "12.45"
print(a.isdigit()) # False .때문에

# startwidth('문자열'): 문자열로 시작하면 True, 아니면 False (대소문자 구분)
a = "Life is too Short"
print(a.startswith('Life')) # True
print(a.startswith('Li')) # True
print(a.startswith('Life i')) # True

# endswidth()
print(a.endswith('Short')) # True
print(a.endswith('ort')) # True














