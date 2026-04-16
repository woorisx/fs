
# r: \\ -> \:(Raw String) 날 머신 문자열
target_path = "C:/suhwo/git/fs/py_basic/ch06_입출력"
base_path = "C:\suhwo/git/fs"
relative_path = "py_basic/ch06_입출력"
full_path = base_path + "/" + relative_path


f = open(full_path+'/foo1.txt', 'w', encoding="UTF-8")
f.write("Life is too short, you need python5")
f.close()

# with문
# f를 자동으로 닫는다.
with open(full_path+'/foo2.txt', "w") as f:
    f.write("Life is too short, you need python6")

    


