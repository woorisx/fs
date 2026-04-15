
# 함수 정의
# 1. 매개변수 있고 반환값 있는 경우
def add(a, b):
    result = a + b 
    return result

# 함수 호출
a = add(3, 4)
print(a) # 7


# 매개 변수가 없다.
def say():
    return "hi"


a = say()
print(a) # hi


#  반환값이 없는 경우
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
    print(f"{a}, {b}의 합은 {a+b}입니다.")

a = add(3, 4)
print(a) # None

# 4. 매개 변수 있고 반환값이 없는 경우
def say():
    print("hi")

say()

# 5. 매개 변수의 순서와 상관없이 매개 변수 이름을 지정하여 호출할 수 있다.
def sub(a, b):
    return a - b
    
result = sub(7, 3)
print(result)

result = sub(a=7, b=3)
print(result)

result = sub(b=3, a=7)
print(result)


