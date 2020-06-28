def calc_long_slice(data):
    temp = [1] * len(data)
    for i, d in enumerate(data):
        for j in range(i):
            if temp[j] <


if __name__ == "__main__":
    data = [10, 9, 2, 5, 3, 7, 101, 18]
    assert 4 == calc_long_slice(data)
