import heapq


def longestSubarray1(A, limit):
    if not A:
        return 0
    max_queue = [A[0]]
    min_queue = [A[0]]
    start, end = 0, 1
    res = 0
    while end < len(A):
        if A[end] >= max_queue[-1]:
            max_queue.append(A[end])
        if A[end] <= min_queue[-1]:
            min_queue.append(A[end])
        end += 1
        while max_queue[-1] - min_queue[-1] > limit:
            if A[start] == max_queue[0]:
                max_queue = max_queue[1:]
            if A[start] == min_queue[0]:
                min_queue = min_queue[1:]
            start += 1
            if not max_queue or not min_queue:
                break
        res = max(res, end - start)
    return res

    """
    记录最大值、最小值的queue

    """


def longestSubarray(A, limit):
    """ 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
    给定一个数组，和一个limit，请找出这个数组的子串中最大值最小值之差不超过limit的最长的子串的长度。
    Example 1:
    Input: nums = [8,2,4,7], limit = 4
    Output: 2
    Explanation: All subarrays are:
    [8] with maximum absolute diff |8-8| = 0 <= 4.
    [8,2] with maximum absolute diff |8-2| = 6 > 4.
    [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
    [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
    [2] with maximum absolute diff |2-2| = 0 <= 4.
    [2,4] with maximum absolute diff |2-4| = 2 <= 4.
    [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
    [4] with maximum absolute diff |4-4| = 0 <= 4.
    [4,7] with maximum absolute diff |4-7| = 3 <= 4.
    [7] with maximum absolute diff |7-7| = 0 <= 4.
    Therefore, the size of the longest subarray is 2.

    Example 2:
    Input: nums = [10,1,2,4,7,2], limit = 5
    Output: 4 
    Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

    Example 3:
    Input: nums = [4,2,2,2,4,4,2,2], limit = 0
    Output: 3

    Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= limit <= 10^9 """
    maxq, minq = [], []
    res = s = 0
    for i, v in enumerate(A):
        heapq.heappush(maxq, (-v, i))
        heapq.heappush(minq, (v, i))
        while -maxq[0][0] - minq[0][0] > limit:
            s = min(maxq[0][1], minq[0][1]) + 1  # 当前的窗口已经不满足题目要求，必须要去掉最大值或者最小值
            while maxq[0][1] < s:
                heapq.heappop(maxq)
            while minq[0][1] < s:
                heapq.heappop(minq)
            res = max(res, i - s + 1)
    return res


import heapq

# 最小堆 从小到大
arr = []
heapq.heappush(arr, (0, 0))
heapq.heappop(arr)
