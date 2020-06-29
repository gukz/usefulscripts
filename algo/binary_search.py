def left_edge(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    if lo < len(arr) and arr[lo] == target:
        return lo
    return -1


assert left_edge([1, 2, 3, 5, 6, 8], 4) == -1
assert left_edge([1, 2, 3, 5, 6, 8], 9) == -1
assert left_edge([1, 2, 3, 5, 6, 8], 8) == 5
assert left_edge([1, 2, 3, 5, 6, 8], 1) == 0
assert left_edge([1, 2, 3, 5, 6, 8], 0) == -1
