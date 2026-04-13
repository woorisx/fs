# 제어문
'''
1. 조건문: if~elif~else, switch(x)~case -> 3.10+ match~case
2. 반복문: for, while
3. 기타: break, contitnue
'''

# if문
'''
if 조건:
    print('택시를 탄다.')
else:
    print('걸어간다.')
'''

# 예) 돈이 있으면 택시를 타고, 없으면 걸어간다.
money = True
money = 2000
card = True

# 조건문 다음에 콜론(:)
# 들여쓰기(indent)
if money > 3000 or card:
    print('택시')
    print('를 ')
    print('탄다.')
else:
    print('걸어간다.')

# in, not in
print(1 in [1, 2, 3]) #True
print(1 not in [1, 2, 3]) #False
print('a' in ['a', 'b', 'c']) #True
print('j' in 'Python') #False
print('P' in 'Python') #True


pocket = ['paper', 'phone', 'money']
if 'money' in  pocket: 
    print('택시 탄다.')
else:
    print('걸어 간다.')

print('=======================')
# pass: 조건문에서 아무 일도 하지 않게 설정(임시 조치)
pocket = ['paper', 'phone', 'money']
if 'money' in  pocket: 
    pass #아무것도 수행되지 않음
else:
    print('걸어 간다.')



pocket = ['paper', 'phone', 'money']
card = True
if 'money' in  pocket: 
    print('택시 탄다.')
else:
    if card:
        print("택시 탄다.")
    else:
        print('걸어 간다.')

# elif(else if)
pocket = ['paper', 'phone', 'money']
card = True
if 'money' in  pocket: 
    print('택시 탄다.')
elif card:
    print("택시 탄다.")
else:
    print('걸어 간다.')


if 'money' in  pocket: print('택시 탄다.')
elif card: print("택시 탄다.")
else: print('걸어 간다.')


print('=======================')

# 성적 예시
grade = "B"
if grade == 'A':
    print("탁월")
elif grade == "B":
    print("우수")
elif grade == "C":
    print("보통")
else:
    print("노력!")



# 파이썬 3.10+
# match~case
grade = "B"
match grade:
    case "A":
        print('탁월')
    case "B":
        print('우수')
    case "C":
        print("보통")
    case _:
        print("노력!")


# 합격 / 불합격
grade = "B"
match grade:
    case "A" | "B" | "C":
        print("합격")
    case _:
        print("불합격")

# 연쇄 비교 연산자

x = 5
print(1 < x)
print(x < 10)

# x는 1보다 크고, 10보다 작다.
print(1 < x and x < 10) #True
print(1 < x < 10) #True


score = 85
if score >= 60:
    result = "합격"
else:
    reult = '불합격'

print(result) #합격

# 조건부 표현식: 둘 중 하나
'''
    변수 = 참일때의 값 if 조건 else 거짓일때의 값
'''
score = 85
result = '합격' if score >= 60 else "불합격"
print(result) #합격





