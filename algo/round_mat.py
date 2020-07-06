"""
对一个二维数组向右旋转90度
"""


def round_mat(mat):
    if not mat:
        return []
    rows, cols = len(mat), len(mat[0])
    res = []
    for col in range(cols):
        col_values = []
        for row in range(rows - 1, -1, -1):
            col_values.append(mat[row][col])
        res.append(col_values)
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
