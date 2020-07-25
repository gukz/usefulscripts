def min_days(bloomDay: list[int], m: int, k: int) -> int:
    """ 5455. Minimum Number of Days to Make m Bouquets
    Given an integer array bloomDay, an integer m and an integer k.
    
    We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
    
    The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
    
    Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
    
    Example 1:
    
    Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
    Output: 3
    Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
    We need 3 bouquets each should contain 1 flower.
    After day 1: [x, _, _, _, _]   // we can only make one bouquet.
    After day 2: [x, _, _, _, x]   // we can only make two bouquets.
    After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
    Example 2:
    
    Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
    Output: -1
    Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
    Example 3:
    
    Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
    Output: 12
    Explanation: We need 2 bouquets each should have 3 flowers.
    Here's the garden after the 7 and 12 days:
    After day 7: [x, x, x, x, _, x, x]
    We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
    After day 12: [x, x, x, x, x, x, x]
    It is obvious that we can make two bouquets in different ways.
    Example 4:
    
    Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
    Output: 1000000000
    Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.
    Example 5:
    
    Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
    Output: 9
    """
    # 大概意思，一个花园，每天会有一批花开放。花店只能采摘连在一起的花。
    # 假设需要提供k束鲜花，每一束需要k朵鲜花。
    # 问至少需要等多少天才能提供？

    """ 思路，很容易想到按照天一天天计算，但是这样会超时
    其实可以换个角度，花越开越多。总有一天可以满足需求。
    因此使用二分查找找到这一天可以减少很多不必要的检索。
    """
    days = sorted(list(set(bloomDay)))
    left, right = 0, len(days) - 1
    while left <= right:
        if left == right:
            return days[left]
        mid = (left + right) // 2
        cur_m = 0
        flow = 0
        for i in bloomDay:
            if i >= days[mid]:
                # 没有开放
                flow = 0
            else:
                flow += 1
            if flow == k:
                # 采摘一束
                cur_m += 1
                flow = 0
        if cur_m >= m:
            right = mid
        else:
            left = mid + 1
    return -1
