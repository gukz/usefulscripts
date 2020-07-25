# 1503. Last Moment Before All Ants Fall Out of a Plank
# https://leetcode.com/contest/weekly-contest-196/problems/last-moment-before-all-ants-fall-out-of-a-plank/
class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        """大概意思是一条线上蚂蚁在走，如果两只蚂蚁碰撞，那么那一调转方向。求多久之后线上无蚂蚁"""
        # 这个题目需要变换思路，蚂蚁碰撞可以看成蚂蚁穿过对方继续前进
        res = 0
        for i in left:
            res = max(res, i)
        for i in right:
            res = max(res, n - i)
        return res
