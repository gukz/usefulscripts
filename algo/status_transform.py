# 状态转换


def count_croak(croakOfFrogs):
    """ croakOfFrogs 0,1,2,3,4

    1,1,2,3,2,

    0 状态4变化过来
    1 状态0变化过来
    2 状态1变化过来
    3 状态2变化过来
    4 状态3变化过来
    """
    status = [0] * 5
    res = 0
    for c in croakOfFrogs:
        last_status = (c - 1 + 5) % 5
        if status[last_status] < 1:
            status[last_status] = 1
        status[last_status] -= 1
        status[c] += 1
        res = max(res, sum(status))
    return res


print(count_croak([4, 0, 0, 2, 3, 1, 4]))
