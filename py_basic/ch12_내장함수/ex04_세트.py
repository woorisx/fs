# set 내장 함수
# add() : 요소추가

s1 = set([1, 2, 3])
s1.add(4)

print(s1) #{1, 2, 3, 4}

# update() : 여러 요소 추가
s1.update([5, 6, 7])
print(s1) #{1, 2, 3, 4, 5, 6, 7}

# remove : 특정 값을 제거
s1 = set([1, 2, 3])
s1.remove(2)
print(s1) #{1, 3}

s1 = set([10, 20, 30])
# s1.remove(40) error 발생
print(s1)

# discard() : 특정값 제거
s1 = set([10, 20 , 30])
s1.discard(20)
print(s1) #{1, 3}
s1.discard(40) #없는 값인데도 에러발생하지 않음
print(s1)

# clear() : 모든 값 제거
s1 = set([10, 20, 30])
s1.clear()
print(s1) #set()

# 기본지식, 베이직한 지식이 현란한 코딩보다 중요하다.






