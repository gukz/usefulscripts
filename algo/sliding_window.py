import re
from collections import defaultdict


def lengthOfLongestSubstring(s):
    if not s:
        return 0
    temp = {s[0]}
    res = 1
    start = 0
    for i in range(1, len(s)):
        while s[i] in temp:
            temp.remove(s[start])
            start += 1
        temp.add(s[i])
        res = max(res, len(temp))
    return res


assert 7 == lengthOfLongestSubstring("abcdaabcdefg")


def minWindow(s, t):
    t_dict = defaultdict(int)
    for c in t:
        t_dict[c] += 1
    c_dict = dict()
    start, end = 0, 0
    res = len(s) + 1

    def contains(dict1, dict2):
        for k, v in dict2.items():
            if k not in dict1:
                return False
            if dict1[k] < v:
                return False
        return True

    while end < len(s):
        if s[end] in c_dict:
            c_dict[s[end]] += 1
        else:
            c_dict[s[end]] = 1
        end += 1
        while contains(c_dict, t_dict):
            res = min(res, end - start)
            if c_dict[s[start]] == 1:
                c_dict.pop(s[start])
            else:
                c_dict[s[start]] -= 1
            start += 1
    return res


assert 5 == minWindow("abcdefffg", "efg")


# [904] https://leetcode.com/problems/fruit-into-baskets/
# 有一排树，你手中有两个篮子，每个篮子只能装一种水果，如果你不摘某个水果那么游戏结束
# 请问你最多能摘多少水果
# 221113332222
# TODO 这个实现是错误的，水果不可以断开
def totalFruit(tree):
    tree = tree + tree
    fruits = [-1, -1]
    amounts = [0, 0]
    index = 0
    res = 0
    while index < len(tree):
        v = tree[index]
        a = 0
        while index < len(tree) and tree[index] == v:
            a += 1
            index += 1
        if v == fruits[0]:
            amounts[0] += a
        elif v == fruits[1]:
            amounts[1] += a
        else:
            if amounts[0] > amounts[1]:
                amounts[1] = a
                fruits[1] = v
            else:
                amounts[0] = a
                fruits[0] = v
        res = max(res, amounts[0] + amounts[1])
    return res


assert 6 == totalFruit([1, 2, 2, 3, 4, 3, 3, 1])


def totalFruitFollowUp(tree, k):
    """找到最多n个不同字符的子串的最长长度"""
    characters = dict()
    start, end = 0, 0
    res = 0
    while end < len(tree):
        char = tree[end]
        end += 1
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
        need_pop = len(characters) > k
        while need_pop:
            s_char = tree[start]
            if characters[s_char] == 1:
                characters.pop(s_char)
                need_pop = False
            else:
                characters[s_char] -= 1
            start += 1
        res = max(res, end - start)
    return res


assert 4 == totalFruitFollowUp([1, 2, 2, 3, 4, 3, 3, 1], 2)

# [30] https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# 给你一个字符串s和一个单词列表，用单词列表可以拼凑出很多字符串，找到这些字符串在s中的起始坐标
def findSubstring(s, words):
    if not words:
        return -1
    w_dict = dict()
    for word in words:
        if word in w_dict:
            w_dict[word] += 1
        else:
            w_dict[word] = 1
    width = len(words[0])
    res = []

    def equal(dict1, dict2):
        if len(dict1) != len(dict2):
            return False
        for k, v in dict2.items():
            if dict1.get(k) != v:
                return False
        return True

    for i in range(width):
        start, end = i, i + width
        c_dict = {}
        while end <= len(s):
            ch = s[end - width : end]
            end += width
            if ch in c_dict:
                c_dict[ch] += 1
            else:
                c_dict[ch] = 1
            if sum(c_dict.values()) == sum(w_dict.values()):
                if equal(c_dict, w_dict):
                    res.append(start)
                first_ch = s[start : start + width]
                start += width
                if c_dict[first_ch] == 1:
                    c_dict.pop(first_ch)
                else:
                    c_dict[first_ch] -= 1
    return res


assert [2, 5] == findSubstring("faabcdefffgabc", ["abc", "ffg", "def"])


# [75] https://leetcode.com/problems/sort-colors/
# 一个数组，红白黄三个球，排序
def sortColors(nums):
    red, white, yell = 0, 0, len(nums) - 1
    while white <= yell:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            continue
        if nums[white] == 1:
            white += 1
            continue
        if nums[white] == 2:
            nums[yell], nums[white] = nums[white], nums[yell]
            yell -= 1
    return nums


assert [0, 0, 1, 1, 1, 2, 2, 2] == sortColors([1, 2, 0, 2, 1, 1, 0, 2])


def find_longest_substr(s):
    res = 0
    characters = set()
    start, end = 0, 0
    while end < len(s):
        while s[end] in characters:
            characters.remove(s[start])
            start += 1
        characters.add(s[end])
        end += 1
        res = max(res, end - start)
    return res


assert 4 == find_longest_substr("asdfdsafassfsdfg")


def reverse_sentence(sent):
    res = []
    start, end = 0, 0
    while end < len(sent):
        if sent[end] == " ":
            res.append(sent[start:end])
            start = end + 1
        end += 1
        if end >= len(sent):
            res.append(sent[start:end])
    reversed_res = []
    for i, _ in enumerate(res):
        reversed_res.append(res[len(res) - i - 1])
    return " ".join(reversed_res)


assert "student a am  I  " == reverse_sentence("  I  am a student")

email_regex = re.compile(
    r"([a-zA-Z0-9_\-]+\.)*[a-zA-Z0-9_\-]+@([a-zA-Z0-9\-]+\.)+[a-zA-Z0-9]{2,6}$"
)
assert email_regex.match("hello@qq.com") is not None
assert email_regex.match("hello@qq.outloo") is not None
assert email_regex.match("hello@qq.outlook") is None
assert email_regex.match("hello@qq.c") is None
assert email_regex.match("hello.microsoft@qq.cc") is not None
assert email_regex.match("hello.microsoft@aa.qq.cc") is not None
