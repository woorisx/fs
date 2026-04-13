# 파이썬 3.11.2
'''
# 시퀀스 : 리스트, 튜플 => 순서(인덱스) 있다.
    리스트: [item1, item2, ...]
    튜플 : ()
# 매핑 : 딕셔너리 -> 순서 없었는데 파이썬 3.7+부터 순서 보장!
   딕셔너리 : {'키1' : 값1, '키2' : 값2, ..}
'''
from main import print_hi

di1 = {
    'name':'alice',
    'age': 30,
    'phone': '010-1234-5678',
    'birth': '1118'
}


# 딕셔너리 쌍{키: 값} 추가하기
a={1:'a'}
# 딕셔너리명[키] = 값
a[2]='b'

print(a)
a['name'] = 'hong'
print(a)

a[3] = [1,2,3]
print(a)


# 키(key)를 사용하여 값(value) 얻기
grade = {'pay':10, 'julliet':99}
print(grade)
print(grade['pay'])
print(grade['julliet'])

# 키는 중복될 수 없다.
# ->하나를 제외한 나머지 키는 무시된다.
a = {1:'a', 1:'b', 1:'c'}
print(a[1])


# 리스트는 키로 사용할 수 없다.
# a = {[1, 2]: 'hi'} error
print(a)


# keys()
# values()
# items()





