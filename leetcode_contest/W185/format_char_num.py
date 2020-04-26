def format_str_num(origin):
    """把一个字符串格式化，使得里面的数字和字母间隔开，如果不能满足，返回空字符串"""
    num, char = list(), list()
    for c in origin:
        if c.isdigit():
            num.append(c)
        else:
            char.append(c)
    if abs(len(num) - len(char)) > 1:
        return ""
    res = ""
    for n, ch in zip(num, char):
        res += f"{ch}{n}"
    if len(char) > len(num):
        res += char[-1]
    if len(char) < len(num):
        res = num[-1] + res
    return res


if __name__ == "__main__":
    inps = ["abcde123", "abcd123", "abcd1234", "abcd12345"]
    ans = ["", "a1b2c3d", "a1b2c3d4", "5a1b2c3d4"]
    for inp, ans in zip(inps, ans):
        assert ans == format_str_num(inp)
