def make_array(*args):
    """返回任意未读的数组，默认值0"""
    if len(args) == 1:
        return [0] * args[0]
    res = list()
    for a in range(args[0]):
        res.append(make_array(*(args[1:])))
    return res


if __name__ == "__main__":
    a = make_array(2, 3)
    assert len(a) == 2
    assert len(a[0]) == 3
