# 문자열을 만드는 방법
print("Hello")
print('Hello')
print('''Life is too short, You need python''')
print("""Life is too short, You need python""")

# 문자열에 작은 따옴표 포함하기
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰 따옴표 포함하기
food = "'Python's favorite food' is perl"
print(food)


# 역슬래시(\)
food = '"Python\'s favorite food" is perl'
print(food)

# 줄바꿈(\n)
food = '"Python\'s favorite food"\n is perl'
print(food)

print('''Life is too short, 
      You need python''')
print("""
      Life is too short, 
      You need python
      """)

# 문자열 연산
head = "Python"
tail = " is fun!"
# 문자열을 연결
print(head + tail)



# 문자열 반복
print(head * 2)

# 문자열의 길이(length): Len()
a = "Life is too short, You need python"
print(len(a))  #34
a = "Life is too short"
print(len(a))  #17

# 문자열 인덱싱과 슬라이싱
# 인덱싱? ~을 가리킨다.
a = "Life is too short, You need python"
print(a[3])
print(a[0])
print(a[-0])
print(a[17])
print(a[-1])
print(a[-2])
print(a[-5])


# 슬라이싱
a = "Life is too short, You need python"
print(a[0:4]) # 0,1,2,3 -> 4이전 , 4포함x
print(a[0:5])
print(a[0:3])
print(a[5:7]) #5, 6
print(a[12:17])

print("--------------------------")
print(a[19:]) # 19부터 끝까지
print(a[:17]) # 처음부터 17이전
print(a[:]) # 모두 출력
print(a) # 모두 출력
print(a[19:-7]) 

# 슬라이싱으로 문자열을 나누기
a = "20260406Sunny" # lucidity : 맑음
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "20260406Sunny" # lucidity : 맑음
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year + "년")
print(day)
print(weather)


#문자열 대체(i->y)
a = "pithon"
print(a[1]) #i
# a[1] = 'y'
# TypeError: 'str' object does not support item assignment
print(a[:1] + 'y' + a[2:])

# 문자열 포맷팅
'''
%d    10진숫자(digit)
%f    실수(float)
%s    문자열(string)
'''
print("I ate %d apples." % 3)
print("I ate %s apples." % "three")

number = 3
print("I ate %d apples." % number)

day = "three"
# 두 개 이상의 값을 넣으려면? 
print("I ate %d apples. so I was sick for %s days." % (number, day))

# %% -> 리터럴(Litteral), 특수문자 %로 지정
print("Error is %d%%." % 3)
print("Error is %f%%." % 3)

print("Error is %")

# 포맷 코드와 숫자 함께 사용하기
print("0123456789")
print("%10s" % "hi")
print("%-10sjane" % "hi") # -는 방향 차이

# 소수점 관련
print("%0.4f" % 3.141592) # 3.1415 / 소수점 이하 4자리까지 표시(반올림)
print("0123456789")
print("%10.4f" % 3.141592) # 전체 10자리 중에 소수점 앞 4자리까지 표시

### v2.6+ format() 함수
print("I eat {0} apples." .format(3))
print("I eat {0} apples." .format("five"))

number = 3
print("I eat {0} apples." .format(number)) #{0} 인덱스 0번부터

print("I ate {0} apples. so I was sick for {1} days." .format(number,day))
print("I ate {1} apples. so I was sick for {0} days." .format(day, number))

# 이름으로 넣기
print("I eat {number} apples. so I was sick for {day} days." .format(number=3, day="five"))


# 정렬(왼쪽, 오른쪽, 가운데)
print("0123456789")
print("{0:<10}" .format("hi"))
print("{0:>10}" .format("hi"))
print("{0:^10}" .format("hi"))


# 공백 채우기
print("{0:=^10}" .format("hi"))
print("{0:!<10}" .format("hi"))
print("{0:->10}" .format("hi"))


# 소수점 표현
y = 3.141592
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# 특수문자 {  } 표시하기
print("{{ and }}" .format()) # { and }

### v3.6+ f문자열 포맷팅
# 현재 파이썬 버전 v3.11.2
name = '홍길동'
age = 30
print('나의 이름은 {name}입니다. 나이는 {age}입니다.'.format(name='김길동', age=24))
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.') # 훨씬 간결한 표현
print(f'나는 내년이면 {age + 1}살이 된다.')


### 딕셔너리
d = {'name':'홍길동', 'age':30} #키와 값의 쌍
print(d)
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.")

# 정렬
print(f'{"hi":<10}') # 왼쪽
print(f'{"hi":>10}') # 오른쪽
print(f'{"hi":^10}') # 가운데

# 공백 채우기
print(f'{"hi":-^10}') # 가운데
print(f'{"hi":!^10}') # 가운데


# 소수점
y = 3.14161592
print(f'{y:0.4f}')
print(f'{y:10.4f}')

# {} 표시
print(f'{{ and }}')

# 천단위 표시
print(f"난 {1500000:,}원이 필요해!")

 


 