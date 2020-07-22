"""
对一个二维数组向右旋转90度
"""


def round_mat(mat):
    width, height = len(mat[0]), len(mat)
    res = []
    for i in range(width):
        line = []
        for j in range(height):
            line.append(mat[j][i])
        res.append(list(reversed(line)))
    return res


mat = [[1, 2, 3], [7, 8, 9], [4, 5, 6]]
print(round_mat(mat))


def str_to_int(s):
    res = 0
    for c in s:
        res *= 10
        res += int(c)
    return res


def ipv4_to_long(ipv4):
    ips = ipv4.split(".")
    res = 0
    for i, ip in enumerate(ips):
        # 1 2 4 8 16 32 64 128 256
        res = res << 8
        res += str_to_int(ip)
    return res


print(ipv4_to_long("0.0.127.1"))
