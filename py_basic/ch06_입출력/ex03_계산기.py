# 계산기
print("==== 간단한 계산기 ====")

# 사용자로부터 두 숫자 입력받기
num1 = int(input('숫자1:'))
num2 = int(input('숫자2:'))


# 계산 결과 출력
print("%d + %d = %d" % (num1, num2, num1 + num2))
print("%d - %d = %d" % (num1, num2, num1 - num2))
print("%d * %d = %d" % (num1, num2, num1 * num2))
print("%d / %d = %d" % (num1, num2, num1 // num2))
print("%d %% %d = %d" % (num1, num2, num1 % num2))
print("%d ** %d = %d" % (num1, num2, num1 ** num2))
