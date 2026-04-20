# 계산기 calculator.py

result = 0
result2 = 0

def add(num):
    global result
    result += num
    return result

print(add(3)) # 3
print(add(4)) # 7(기존의 3을 갖고 있다가 더해줌)


result2 = 0

def add2(num):
    global result2
    result2 += num # 결과값 반환(result)에 입력값(num) 더하기
    return result2

print(add2(3)) # 3
print(add2(7)) # 7(기존의 3을 갖고 있다가 더해줌)


# 클래스  
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result
    

# 객체 : calc1, calc2
# 객체(Object)란 클래스로 만든 피조물(과자 틀로 찍어낸 과자)을 뜻한다.
# 객체마다 고유한 성격을 가진다.
# 클래스로 만든 객체를 '인스턴스'라고도 한다.
# a = Cookie()
# a는 객체이다.
# a는 Cookie 클래스로 만든 인스턴스이다.

calc1 = Calculator()
calc2 = Calculator()


print(calc1.add(3))
print(calc1.add(4))
print(calc2.add(3))
print(calc2.add(7))

