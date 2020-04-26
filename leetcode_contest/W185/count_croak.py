def c2i(c):
    return {"c": 0, "r": 1, "o": 2, "a": 3, "k": 4}.get(c)


def count_croak(croakOfFrogs):
    "数青蛙个数，看成多线程打印字符串。每个线程处于一个状态
    r表示一个线程从状态c切换成状态r
    记录每个状态有多少线程，然后进行状态切换，统计当前时刻一共有多少个线程，
    线程最大值就是需要的线程个数

    初始状态不需要从旧状态转换而来
    末尾状态在统计完后可以清空
    "
    if not croakOfFrogs:
        return 0
    all_croaks = [0] * 5
    res = 0
    for c in croakOfFrogs:
        i = c2i(c)
        if i is None:
            return -1
        if i > 0:
            all_croaks[i - 1] -= 1
        all_croaks[i] += 1
        for croak in all_croaks:
            if croak < 0:
                return -1
        res = max(res, sum(all_croaks))
        all_croaks[4] = 0  # 叫过后就可以结束了
    if any(all_croaks):
        return -1
    return res


if __name__ == "__main__":
    inp_list = ["croakcroak", "croac", "crcoakroak"]
    res_list = [1, -1, 2]
    for inp, res in zip(inp_list, res_list):
        assert res == count_croak(inp)
