'''
shutil.copy(src, dst)
shutil.copytree(src, dst)
'''
import shutil
from pathlib import Path

def copy_file_example(base:Path):
    src_file = base / "spam" / "file1.txt"

    # 디렉토리에 복사 (dst => 디렉토리)
    copied1 = shutil.copy(src_file, base)
    print("결과:", copied1)

    # 파일명 지정 복사
    copied2 = shutil.copyfile(src_file, base / "spam" / "file2.txt")
    print("결과:", copied2)


def copy_tree_example(base:Path):
    # spam 디렉토리 전체를 spam_backup으로 복사
    dst = base / "spam_backup"

    if dst.exists():
        shutil.rmtree(dst)

    copied_tree = shutil.copytree(base / "spam", dst)
    print("copy tree 결과:", copied_tree)



if __name__ == "__main__":
    base = Path.cwd() / "연습"
    copy_file_example(base)

    copy_tree_example(base)