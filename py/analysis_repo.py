#!/usr/bin/python3
from collections import defaultdict
import fire
import os


def get_file_len(path):
    print(path)
    return int(os.popen(f"wc -l {path}").read().split()[0])


temp = defaultdict(int)


def walk_files(path, suffix):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            if "test" in f.lower():
                continue
            if f.endswith(suffix):
                total += 1
                l = get_file_len(os.path.join(root, f))
                temp[l//50] += 1
    a = [(k, v) for k, v in temp.items()]
    a.sort(key=lambda x: -x[1])
    print("\nGenerate report:")
    print(f"{total}\tTotal.")
    for i in a[:10]:
        print(f"{i[1]}\tlength: {i[0]*50}~{i[0]*50+50}")


if __name__ == "__main__":
    fire.Fire(walk_files)
