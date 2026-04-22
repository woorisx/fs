# 오류 일부러 발생시키기

# 부모클래스
class Bird:
    def fly(self):
        raise NotImplementedError
    
# 자식클래스
class Eagle(Bird):
    # pass
    # 메서드 재정의 
     def fly(self):
        print("Very fast")

eagle = Eagle()
eagle.fly()




# 예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


say_nick("천사")
say_nick("바보")
