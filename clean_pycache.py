import fire
import os
import shutil


def walk_files(path):
    for root, dirs, _ in os.walk(path):
        for pydir in dirs:
            if pydir == "__pycache__":
                try:
                    shutil.rmtree(os.path.join(root, pydir))
                except PermissionError:
                    print(os.path.join(root, pydir))


if __name__ == "__main__":
    fire.Fire(walk_files)
