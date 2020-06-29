def get_all_order(arr):
    res = []

    def dfs(arr, curIndex):
        if curIndex == len(arr):
            res.append(arr[:])
            return

        for i in range(curIndex, len(arr)):
            arr[curIndex], arr[i] = arr[i], arr[curIndex]
            dfs(arr, curIndex + 1)
            arr[curIndex], arr[i] = arr[i], arr[curIndex]

    dfs(arr, 0)
    return res


assert len(get_all_order([1, 2, 3])) == 6


def use_coins(coins, target):
    res = []
    coins.sort()

    def dfs(index, cur, target):
        if target < 0:
            return
        if index == len(coins):
            if target == 0:
                res.append(cur)
            return
        for i in range((target // coins[index]) + 1):
            dfs(index + 1, cur + [i], target - coins[index] * i)

    dfs(0, [], target)
    return res


assert len(use_coins([1, 2, 4], 14)) == 20
