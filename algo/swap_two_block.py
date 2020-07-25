def swap_two_block(data, s1, e1, s2, e2):
    """假设没有交叉8:46 8:57 s1 < s2"""
    data = data[:]
    temp1 = data[s1:e1]
    mid = data[e1:s2]
    for i in range(s2, e2):
        data[s1 + i - s2] = data[i]
    for i in range(e1, s2):
        data[s1 + e2 - s2 + i - e1] = mid[i - e1]
    for i in range(s1, e1):
        data[e2 - e1 + i] = temp1[i - s1]
    return data


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    s_data = swap_two_block(data, 2, 5, 7, 9)
    assert [1, 2, 8, 9, 6, 7, 3, 4, 5, 0] == s_data
