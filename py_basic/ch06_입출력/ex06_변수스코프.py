# 변수 스코프
def my_function():
    func_var = "함수 안의 변수"
    print(func_var)

my_function()

if True:
    if_var = "if 블록 안의 변수"

print(if_var)

for i in range(3):
    loop_var = "for 반복문 안의 변수"

print(i)
print(loop_var)

with open("C:/suhwo/git/fs/py_basic/ch06_입출력/test.txt", "w") as f:
    content = "Hello Python!"
    f.write(content)

print(content)