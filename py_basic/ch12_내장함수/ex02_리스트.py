# 내장 함수
# append() : 요소 추가, 맨 마지막에 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)

# insert(인덱스, 아이템): 요소 삽입
a =[1, 2, 3]
a.insert(0, 4) # 0번째 인덱스에 4를 추가
print(a)
a.insert(3, 5) #원래 배열이 밀려나면서 추가됨
print(a)

# remove(값) : 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3) #왼쪽에서 읽어내면서 첫번째 값 하나만 삭제
print(a)

# pop() : 마지막 요소 꺼내기
a = [1, 2, 3]
print(a.pop())
print(a)

# pop(인덱스): 인덱스에 해당하는 요소를 꺼냄
a = [1, 2, 3]
print(a.pop(1))
print(a)


#  count(값) : 아이템(항목) 개수
a = [1, 2, 3, 1, 2, 1, 1]
print(a.count(1)) # 4, 1은 모두 4개가 있음

# extend() : 리스트 확장
a = [1, 2, 3]
print(a)
# a.extend([4, 5])
a += [4, 5]
print(a)
b = [6, 7]
a.extend(b)
print(a)


print('----------------')

# sort() : 정렬(오름차순, 내림차순)
a = [1, 4, 3, 2]
print(a)
a.sort()
print(a)

a = ['b', 'c', 'a']
a.sort()
print(a)


# reverse() : 역순
a.reverse()
print(a)

# 내림차순
a = [1, 4, 3, 2]
a.sort()
print(a)
a.reverse()
print(a)

# index(항목): 인덱스 변환
a = [1, 2, 3]
a = [10, 5, 31]
print(a.index(31)) # 3이 몇번째 인덱스인가
print(a.index(5))
