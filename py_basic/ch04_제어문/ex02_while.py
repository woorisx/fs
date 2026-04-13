# while문 
# do while없음
'''
    while 반복문:
        실행문1
        실행문2
        ...

'''



# 예제 : 나무 10번 찍기
tree_hit = 0
while tree_hit < 10:
    tree_hit = tree_hit + 1
    print("나무를 %d번 찍었습니다." % tree_hit)
    if tree_hit == 10:
        print("나무가 넘어갑니다.")  


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:"""


number = 0
while number != 4:
    print(prompt)
    number = int(input())