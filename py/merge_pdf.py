import fire
from PyPDF2 import PdfFileMerger
import os


def walk_files(path, file_handler):
    for root, dirs, files in os.walk(path):
        for f in files:
            file_handler(os.path.join(root, f))


merger = PdfFileMerger()


def handler(p):
    if p.endswith(".pdf"):
        merger.append(open(p, "rb"))


def merge(mypath):
    walk_files(mypath, handler)
    with open('merged.pdf', "wb") as fout:
        merger.write(fout)


if __name__ == "__main__":
    fire.Fire(merge)
