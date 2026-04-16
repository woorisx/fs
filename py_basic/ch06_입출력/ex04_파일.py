# 1. 파일 생성
'''
    파일 열기 모드
    r : read(읽기)
    w : write(쓰기)
    a : append(추가)
'''
   
'''
    \n
    \t
    \'
    \"
    \\

    절대경로  
    http://
    https://
    C:~
    D:~
'''

# 절대 경로
# f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "w")
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "w")
f.write("Life is too short, you need python2\n")
f.close()

# 2. 파일 쓰기
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "w", encoding="UTF-8")
f.write("Life is too short, you need python4\n")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 3. 파일 읽기
'''
    read() : 파일의 전체 내용을 문자열로 읽기
    readline() : 파일의 (첫)한 줄을 문자열로 읽기
'''
# 모든 글 읽기
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "r", encoding="UTF-8")
data = f.read()
print(data)
f.close()


# 한줄 읽기
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "r", encoding="UTF-8")
line = f.readline()
print(line)
f.close()

# 한줄이 있으면 읽고 출력 반복
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "r", encoding="UTF-8")
while True:
    line = f.readlines()
    if not line: break
    print(line)
f.close()

# for문으로 한줄씩 읽는다
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "r", encoding="UTF-8")
lines = f.readline()
print(lines)
for line in lines:
    print(line)
f.close()


# strip():공백제거
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "r", encoding="UTF-8")
lines = f.readlines()
print(lines)
for line in lines:
    print(line.strip())
f.close()


f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "r", encoding="UTF-8")
for line in f:
    print(line.strip())
print("=======")
f.close()

# 4. 내용 추가
f = open("C:\\suhwo\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "a", encoding="UTF-8")
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()






