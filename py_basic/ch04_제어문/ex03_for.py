# 반복문
# for문
# 시퀀스 : 리스트, 튜플, 문자열, range() 등
'''
    for 변수 in 시퀀스:
        실행문
'''
# for 변수 in 시퀀스:
#     실행문

lst = ['one', 'two', 'three']
for i in lst:
    print(i)

'''
one
two
three
'''

a = [(1, 2),(3, 4),(5,6 )]
for(first, last) in a:
    print(first+last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)



# continue문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue # for로 돌아감
    print("%d번 학생 축하합니다. 합격입니다." % number)

# range(시작, 끝) 함수
a = range(10)
print(a) # ragne(0, 10)


# 1부터 10까지 합
# range(1, 11) : 1, 2, 3, ....., 10
sum = 0
# for i in [1, 2, 3, .., 10]
for i in range(1, 101):
    sum += i # i값을 sum에 누적해서 합함
print(sum)


# 합격 축하 문장 출력
# len(요소): 요소의 개수
# range(5) : 0, 1, 2, 3, 4 -> range(0, 5)
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


# print(값)
# end의 기본값은 줄바꿈(\n)
print("Hello", end="\n")
print("Hello")
print("Hello")
print("Hello", end=" ")
print("Hello", end=" ")
print("Hello")


# 중첩 for문
# 구구단

for i in range(2, 10): # 단수 : 2 ~ 9단
    for j in range(1, 10): # 1 ~ 9
        print(i,"*", j, "=", i*j, end=" \n")
    print('') # 줄바꿈

'''
2 * 1 = 2 
2 * 2 = 4 
2 * 3 = 6 
2 * 4 = 8 
2 * 5 = 10 
2 * 6 = 12 
2 * 7 = 14 
2 * 8 = 16 
2 * 9 = 18 

...

9 * 1 = 9 
9 * 2 = 18 
9 * 3 = 27 
9 * 4 = 36 
9 * 5 = 45 
9 * 6 = 54 
9 * 7 = 63 
9 * 8 = 72 
9 * 9 = 81 
'''

# 리스트의 각 항목에 3 곱하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result) # [3, 6, 9, 12]

# 반복문 간소화
# list Comprehension(컴프리핸션)
# 시퀀스(반복가능객체):리스트, 튜플, 문자열, range()
'''
    [표현식 for 항목 in 시퀀스 [if 조건문]if생략가능]
'''
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result) # [3, 6, 9, 12]

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]


# 구구단
result = [x * y for x in range(2, 10) 
          for y in range(1, 10)]
print(result)


# break문
for i in range(10):
    if i == 5:
        break
    print(i)

# for ~ else
for i in range(5):
    print(i)
else:
    print("for문이 정상 종료됩니다.")

# enumerate : 열거하다.
# -> 0부터 시작하는 인덱스 번호를 자동 생성
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, 1):
    print(f"{i} : {fruit}")


# zip() : 두 개 이상의 리스 동시 순회
names = ['홍길동', '김철수', '이영자']
scores = [85, 92, 73]
for name, score in zip(names, scores):
    print(f"{name} : {score}점")


