# 리스트(list, 목록) 자료형 연습

odd = [1, 3, 5, 7, 9] # 홀수 목록
a = []
print(a)
a = list()
print(a)
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1,2,['Life', 'is']]

# 인덱싱
b = [1,2,3]
print([0]) # 1
print(b[0]+b[2])
print(b[-1])


e = [1, 2, 3, ['a', 'b', 'c']]
print(e[0])
print(e[-1])
print(e[3])

print(e[-1][0]) 
print(e[-1][1])
print(e[-1][2])

e = [1, 2, 3, ['a', 'b', ['Life', 'is']]]

print(e[-1][-1][0])
print(e[3][2][0])


# 슬라이싱 
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[:2])
print(a[2:]) 
print(a[:])
print(a)

e = [1, 2, 3, ['a', 'b', 'C'], 4, 5]
print(e[2:5])


# 리스트 연산
a  = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
c = a + b
print(c)
print(a*3)
print(len(a))

a = [1, 2, '3']
print(a[2]+'hi')

a = [1, 2, '3']
print(str(a[2])+'hi') 



# 리스트 수정, 삭제

a  = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)    

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)
