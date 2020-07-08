res = []


def dfs(arr, curIndex):
    if curIndex == len(arr):
        res.append(arr[:])
    for i in range(curIndex, len(arr)):
        arr[curIndex], arr[i] = arr[i], arr[curIndex]
        dfs(arr, curIndex + 1)
        arr[curIndex], arr[i] = arr[i], arr[curIndex]


dfs([1, 2, 3], 0)
print(res)
