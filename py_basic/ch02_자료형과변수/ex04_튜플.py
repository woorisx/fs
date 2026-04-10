# 튜플(Tuple)
# 리스트(List)와 다른점

'''
리스트: [item1, item2, ...]
튜플: (item1, item2, ...)
    요솟값을 바꿀 수 없다.
'''
from main import print_hi

ls1 = []
ls1 = [10]
ls1 = [1,2,3]
print(ls1)

tu1 = ()
# 하나의 요소일 떄 요소 끝에 ','를 찍는다.
tu1 = (10,)
tu1 = (1,2,3)
# 소괄호 생략 가능
tu1 = 1,2,3
tu1 = (1,2,3, ('a', 'b', 'c'))
print(tu1)

# 인덱싱
tu1 = (18,20,30, ('a', 'b', 'c'))
print(tu1[0 ])
print(tu1[2 ])

# 튜플은 요소값을 삭제할 수 없다.
# del tu1[2] #error


tu1 = (10,20,30,('a', 'b', 'c'))
# print(tu1[0]=100)

# 슬라이싱
tu1 = (1,2,3, 'a', 'b', 'c')
print(tu1[2:4])
print(tu1[:4])
print(tu1[2:])
print(tu1[:])
print(tu1)

# 튜플 더하기
tu1 = (1, 2, 'a', 'b')
tu2 = (3, 'c')
tu3 = tu1 + tu2
print(tu3)


# 튜플 곱하기
tu1 =(1,2)
tu2 = tu1 *3
print(tu2)

# 튜플 길이 구하기
t1 =(1,2,3)
print(len(t1))