# 표준 출력
'''
    print(값, 값, ..., 값, sep=' ', end='\n')
    sep는 구분자로 기본값은 공백
    end는 끝맞추기 기본값은 \n
'''
# print()
# sep의 기본값은 공백
print("Life is too short")
print("Life", "is", "too", "short")
# 모두 문자열이면 +는 연결
# 문자열과 숫자의 +는 에러
print("Life" + "is" + "too" + "short")
print("Life", "is", "too", "short", sep=":")
print("2026", "04", "16", sep="-")

'''
Life is too short
Life is too short
Lifeistooshort
Life:is:too:short
'''

# end의 기본값 \n
print("Life", end="\n")
print("is")
print("too")
print("short")
# Life is too short

print("Life", end=" ")
print("is", end=" ")
print("too", end=" ")
print("short")
# Life is too short

for i in range(5):
    print(i, end=" ")


