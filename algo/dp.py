def lengthOfLIS1(nums):
    temp = [0] * len(nums)
    res = 0
    for i, num in enumerate(nums):
        max_len = temp[0]
        for j in range(0, i):
            if nums[j] <= num:
                max_len = max(max_len, temp[j])
        temp[i] = max_len + 1
        res = max(res, temp[i])
    return res


assert 4 == lengthOfLIS1([1, 3, 5, 2, 4, 7])


# [72] https://leetcode.com/problems/edit-distance/
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
# TODO 最小编辑距离
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(2)]
    return dp


# [375] https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.
# Bottom-up dynamic programming
# TODO
def getMoneyAmount(n):
    pass


# [562] https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
# compress to 2D DP
# TODO
def longestLine2(M):
    pass


# [188] https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# 买卖股票，最多交易K次
def maxProfit(k, prices):
    """
    状态：已购、未购买、剩余交易次数
    """
    p = len(prices)
    dp = int[p][2][k]
    #  dp[p][0][m] = max(dp[p - 1][0][m], dp[p - 1][1][m - 1] - prices[p])
    #  dp[p][1][m] = max(dp[p - 1][1][m], dp[p - 1][0][m] + prices[p])
