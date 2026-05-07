import os
from pathlib import Path

def make_sample(root: Path):
    # 폴더 생성
    (root / 'spam').mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs").mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs" / "bacon").mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs2").mkdir(parents=True, exist_ok=True)

    for f in ["spam/file1.txt", "spam/file2.txt", "spam/eggs/file3.txt", "spam/eggs/bacon/file4.txt"]:
        (root / f).write_text("Hello", encoding="utf-8")

def show_list_str(root:Path):
    full_path = str(root / "spam")
    
    print(f"{full_path} 목록 :")
    print("-"*20)

    # 첫번쨰 방법 : os.list_dir 경로를 문자열로 변환

    for p in os.listdir(full_path):
        print(p)
        print("="*20)

def show_list_path(root:Path):
    # Path.iterdir
    full_path = root / "spam"
    
    print(full_path.iterdir())
    # <map object at 0x000002340099E020>: 16진수로된 주소값
    print("-"*20)

    for p in full_path.iterdir():
        # 두번째 방법 -> Path.iterdir() -> 경로 인식(변환필요x)
        if p.is_dir():
            # 만약 폴더이면 True, 아니면 False
            print(f"[{p}]")
        else:
            print(f"{p}")

# if __name__ == "__main__":
# 이 파일이 직접 실행된 것인지, 아니면 다른 파일에 의해 불러와진(import)것인지 구분하는 역할이다.
# __name__: 현재 실행 중인 모듈(파일)의 이름, 자기 자신
if __name__ == "__main__":
    base = Path(__file__).parent / "연습"
    
    make_sample(base)
    show_list_str(base)
    show_list_path(base)