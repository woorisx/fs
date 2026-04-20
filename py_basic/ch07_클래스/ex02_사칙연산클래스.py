# 사칙연산 클래스


# 1. 클래스를 어떻게 만들지 먼저 구상
'''
1.클래스명: FourCal
2.메서드명
    setdata() : 두 수를 지정
    add() : 두 수의 합
    sub() : 두 수의 차
    mul() : 두 수의 곱
    div() : 두 수의 나머지

a = FourCal()
a.setdat(4, 2)
a.add()
a.sub()
a.mul()
a.div()
    
'''

# 2. 클래스의 구조를 만든다.
# 클래스 안에 구현된 함수는 다른 말로 메서드(method)라고 부른다.
# 메서드의 첫번째 매개변수 self는 특별한 의미를 가진다. 매개변수 이름은 관례적으로 self를 사용한다. 객체의 메서드를 호출할 때 호출한 객체 자신이 전달된다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
b = FourCal()
print(type(a)) # <class '__main__.FourCal'>
# 객체 a가 FourCal의 
# 3.객체 만들기
# a = FourCal()
# 객체 a가 
a.setdata(4, 2)
b.setdata(3, 7)

# 객체에 생성되는 변수를 인스턴스 변수 또는 속성이라고 부른다.
print(a.first) # 4
print(a.second) # 2
print(b.first) # 3
print(b.second) # 7

print(a.add()) # 6
print(a.sub()) # 2
print(a.mul()) # 8
print(a.div()) # 2.0

print(b.add()) # 10
print(b.sub()) # -4
print(b.mul()) # 21
print(b.div()) # 0.42



