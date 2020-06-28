def trap_water(data):
    temp = [0] * len(data)
    curMax = data[-1]
    for i in range(len(data)):
        curMax = max(curMax, data[len(data) - 1 - i])
        temp[len(data) - 1 - i] = curMax
    res = 0
    curMax = data[0]
    for i, val in enumerate(data):
        min_height = min(curMax, temp[i])
        if min_height > val:
            res += min_height - val
        curMax = max(curMax, val)
    return res


if __name__ == "__main__":
    data = [5, 2, 4, 7, 6, 4, 5]
    assert 5 == trap_water(data)
