# 클래스 변수
class Family:
    # 클래스 안에 변수를 선언하여 생성한다.
    lastname = "잭슨"

# 클래스_이름.클래스변수로 사용
print(Family.lastname)

# 객체 변수
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

# 클래스 변수와 객체 변수
# a 객체에 lastname이라는 객체변수가 새롭게 생성된다.
Family.lastname = "김"
a.lastname ="최" 
print(a.lastname) #최

print(Family.lastname) #김
print(b.lastname) #김




