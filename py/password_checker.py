#!/usr/bin/python3
from nltk.corpus import wordnet
import fire
import os


# 检查代码里是否包含敏感信息，比如秘钥之类的。检查思路就是英文字母序列必须是某个英文单词。


white_words = ["rpc", "pb2"]


def split(line):
    split_chars = ":/,. _-()[]{}\"''+*/&%#!="
    start, end = 0, 0
    while end < len(line):
        if line[end] in split_chars:
            if end > start:
                yield line[start:end]
            start = end + 1
        end += 1


temp = set()


def validate_files(file_path):
    for line in open(file_path, "r", encoding="utf-8"):
        words = list(split(line))
        for w in words:
            if len(w) < 8 or w.isdigit():
                continue
            if not wordnet.synsets(w):
                temp.add(w)


def walk_files(path="."):
    for root, _, files in os.walk(path):
        if "__pycache__" in root:
            continue
        for f in files:
            try:
                validate_files(os.path.join(root, f))
            except UnicodeDecodeError:
                print("decode error for", os.path.join(root, f))
    print(temp)


if __name__ == "__main__":
    fire.Fire(walk_files)
