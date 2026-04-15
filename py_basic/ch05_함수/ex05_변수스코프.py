# 범위, 영역:변수(variable)의 scope(스코프)
# var a = 1 (자바스크립트)
# const a = 1 (자바스크립트)
# let a = 1 (자바스크립트)


a = 1
def vartest(a):
    a += 1
    print(f"함수 내의 {a} 출력")

vartest(a)
print(f"함수 밖의 {a} 출력") # 1




# global 키워드
b = 1
def vartest2():
    global b
    b += 1
    print(f"함수 밖의 b출력:{b}") # 1

vartest2()
print(f"함수 밖의 b출력:{b}") # 2 


# 리스트 : 요소를 추가하면 리스트의 마지막에 추가된다.
# 리스트는 아이템(항목)이 변경 가능한 자료형(mutable)/immutable:변경 불가능
# 리스트와 딕셔너리를 함수로 전달할 때는 원본이 변경될 수 있다. 
def change_list(my_list):
    my_list.append(4)

a = [1, 2, 3]
change_list(a)
print(a)


