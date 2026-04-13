#  set(집합)
'''
1.{item1, item2, ..}
2. 중복 없다.
3. 순서없다. --> 인덱싱 불가능
4. mutable한 자료형 -> 요소 추가, 제거 가능
5. 집합 연산을 지원(합집합, 교집합, 차집합 등) 
6. set은 {}가 아니라, 빈 set은 {}가 아니라 set()로 표현합니다.

참고 
딕셔너리 형식
    {key1: value1, key2: value2, ...}
'''

s1 = {1, 2, 3}

print(s1)

s1={}
print(s1)

# type(): 데이터 타입 확인

print(type(s1))


s2 = set()
print(s2)
print(type(s2))


s2 = {'H', 'e', 'l', 'l', 'o'}
print(s2) #{'o', 'e', 'H', 'l'} 중복 제거

s2 = set('Hello')
print(s2) # {'e', 'H', 'o', 'l'} 중복 제거

# 리스트나 튜플을 set으로 변환
s3 = set([1, 2, 3, 4, 5, 5])
print(s3) #{1, 2, 3, 4, 5}


# set을 list로 변환
lst = list(s3)
print(lst)  # [1, 2, 3, 4, 5]

# set을 tuple로 변환
t = tuple(s3)
print(t) # (1, 2, 3, 4, 5)

# 집합
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

# 합집합 A | B
print(s1 | s2) #{1, 2, 3, 4, 5, 6, 7, 8}
# 교집합 A & B
print(s1 & s2) #{4, 5}
# 차집합 A - B
print(s1 - s2) #{1, 2, 3}
print(s2 - s1) #{8, 6, 7}

