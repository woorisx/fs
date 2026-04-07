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
print(a[12])
print(a[-1])
print(a[-2])
print(a[-5])


# 슬라이싱
print(a[0:4]) # 0,1,2,3 -> 4이전 , 4포함x
print(a[0:5])
print(a[0:3])
print(a[5:7])
print(a[12:17])