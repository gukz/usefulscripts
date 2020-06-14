def max_zero_slice(data):
    sums = {}
    total = 0
    res = 0
    for i, v in enumerate(data):
        total += v
        if total in sums:
            res = max(res, i - sums[total])
        else:
            sums[total] = i
    return res


if __name__ == "__main__":
    a = [5, 1, -1, 1, -1, 5, 6, 7, -9, 2, 2]
    v = max_zero_slice(a)
    assert 4 == v
