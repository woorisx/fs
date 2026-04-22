

# import os
# current_dir = os.path.dirname(__file__)
# print(current_dir)
# # process_scores.py



# students = ["김철수", "이영희", "박민수", "최유진"]

# for student in students:
#     # 현재 폴더 경로와 파일명을 결합
#     file_path=os.path.join(current_dir, f"{student}_성적.txt")
#     try:
#         with open(file_path, 'r', encoding="UTF-8") as f:
#             score = f.read()
#             print(f"{student}의 성적: {score}")
#     except FileNotFoundError:
#         print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
#         continue  # 다음 학생으로 넘어감




# 파이썬 3.4+
from pathlib import Path

students = ["김철수", "이영희", "박민수", "최유진"]

# 현재 파일을 기준으로 경로 설정
current_dir = Path(__file__).parent
print(current_dir)
# C:\suhwo\git\fs\py_basic\ch10_예외처리

for student in students:
    # 현재 폴더 경로와 파일명을 결합
    file_path=current_dir / f"{student}_성적.txt"
    try:
        with open(file_path, 'r', encoding="UTF-8") as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        continue  # 다음 학생으로 넘어감


# 오류를 완전히 무시하고 싶을 때도 있다.
# error_pass.py
try:
    # 설정 파일을 읽으려 시도
    with open("설정파일.txt", 'r') as f:
        config = f.read()
except FileNotFoundError:
    pass  # 설정 파일이 없어도 계속 진행

# 프로그램의 주요 기능은 계속 수행
print("프로그램이 정상적으로 실행됩니다.")

