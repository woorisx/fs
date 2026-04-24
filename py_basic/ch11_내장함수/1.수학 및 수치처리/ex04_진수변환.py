value = 255

# 10진수 -> 각 진수 문자열
b_str = bin(value)  # '0b11111111' 10진수 -> 2진수
o_str = oct(value)  # '0o377' 10진수 -> 8진수
h_str = hex(value)  # '0xff'  10진수 -> 16진수

print(f"2진수: {b_str}, 8진수: {o_str}, 16진수: {h_str}")

# 각 진수 문자열 -> 10진수 정수
print(int(b_str, 2))   # 255
print(int(o_str, 8))   # 255
print(int(h_str, 16))  # 255

# format 함수를 이용한 진수 변환 (숫자만)
print(f"16진수 숫자만: {format(value, 'x')}")  # 'ff'