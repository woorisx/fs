
def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result) # 7. 12

result1, result2 = add_and_mul(3, 4)
print(result1, result2) # 7, 12
print(result1) # 7
print(result2) # 12


def add_and_mul(a, b):
    return a + b
    return a * b # 죽은 코드 (에러발생x)


result = add_and_mul(2, 3)
print("결과는 : ", result) # 5

def say_nick(nick):
    if nick == '야호':
        return
    print("나의 별명은 %s입니다." % nick)
    

say_nick("야호")
say_nick("야흐")





