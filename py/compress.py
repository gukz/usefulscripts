import lzma
import zlib


def compress(data: bytes) -> bytes:
    return lzma.compress(
        data, format=lzma.FORMAT_RAW, filters=[{"id": lzma.FILTER_LZMA2}]
    )


def decompress(data: bytes) -> bytes:
    return lzma.decompress(
        data, format=lzma.FORMAT_RAW, filters=[{"id": lzma.FILTER_LZMA2}]
    )


if __name__ == "__main__":
    data = "你好世界".encode("utf")
    print("origin", list(a for a in data))
    print(list(a for a in compress(data)))
    print(zlib.crc32(compress(data)))
