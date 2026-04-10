



# 딕셔너리 관련 함수

'''
    {key:value}
'''


a = {
    'name':'hong',
    'age':20,
    'phone':'010-1234-5678',
    'birth':'1118',
    'address':'성남시 분당구'
}



# Keys()

print(a.keys())
print(list(a.keys()))
# values()
print(a.values())
print(list(a.values()))

# items()
print(a.items())
# dict_items([('name', 'hong'), ('age', 20), ('phone', '010-1234-5678'), ('birth', '1118')])
print(list(a.items()))
# [('name', 'hong'), ('age', 20), ('phone', '010-1234-5678'), ('birth', '1118')]

# clear(): 아이템 삭제
# a.clear()
# print(a)

# get():keys로 value  열기
print(a['name'])
# get
print(a.get('name'))

# 없는 키를 사용하면?
# print(a['address']) error
# print(a.get('address')) NONE

# get(키, [기본값])
print(a.get('address', ' 경기도 성남시 분당구'))

# in 키워드 : 키의 유무, 있으면 True, 없으면 false
print('name' in a)  # True
print('zipcode' in a) # False

# pop(키) : 키에 해당하는 아이템 뽑기
phone = a.pop('phone')
print(phone)
print(a)
# {'name': 'hong', 'age': 20, 'birth': '1118', 'address': '성남시 분당구'} pop()함수로 phone키와 값을 제외시킴

email = a.pop('email', '정보없음')
print(email)
print(a)
