class FourCal:
    # 생성자
    def __init__(self, first, second):
        # 인스턴스 변수
        self.first = first
        self.second = second
        
    # 메서드(method)
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
   

# 상속(Inheritance)란 '물려받다'라는 뜻
# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
'''
    class  클래스_이름(상속할_클래스_이름)
        pass
'''

class MoreFourCal(FourCal): # 다중상속 가능 ','처리 후 작성
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add()) # 6
print(a.sub()) # 2
print(a.mul()) # 8
print(a.div()) # 2.0
print(a.pow()) # 16

# 내장 함수
print('-' * 30)
print(pow(2, 3)) # 8
print(2**3) # 8
print(pow(10, -1)) # 0.1
print(10 ** -1) # 0.1
print(pow(2, 10, 7)) # (2 ** 10) % 7 -> 1024 % 7(나머지를 구함) -> 2


#  파이썬은 다중상속 가능

class Mother:
    def skill(self):
        print('요리실력')

class Father:
    def hobby(self):
        print('축구시청')


class child(Mother, Father): #중요.. 다중 상속 예제
    def game(self):
        print("게임시청")

c = child()
c.skill() #요리실력
c.hobby() #축구시청
c.game() #게임시청

