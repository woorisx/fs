'''
os.unlink
os.rmdir
shutil.rmtree
'''
import os
from pathlib import Path
from tkinter import Y

def prepare_demo(base:Path):
    d = base / "연습" / "dryrun"
    d.mkdir(parents=True, exist_ok=True)

    for name in ["note.rxt", "temp.rxt"]:
        (d / name).write_text("샘플", encoding="utf-8")

    return d

def find_targets(demo:Path, param:str):
    return list(demo.glob(param))

def delete_with_dry_run(files, really:bool):
    for f in files:
        if really:
            os.unlink(f) # 실제 삭제
            print(f"[삭제] {f}")
        else:
            print(f"[삭제 예정] {f}")

if __name__ == '__main__':
    # base = Path.cwd() #작업폴더
    base = Path(__file__).parent #현재 폴더

    demo = prepare_demo(base)

    targets = find_targets(demo, "*.rxt")
    print(targets)

    delete_with_dry_run(targets, really=False)

    yn = input("해당 파일을 지울까요? y(es)/n(o) >")
    if yn.lower() == "y":
        delete_with_dry_run(targets, really=True)