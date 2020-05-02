from utils import make_array


def ans115(S, T):
    """ Given a string S and a string T, count the number of distinct subsequences of S which equals T.
    A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
    
    Example 1:
    
    Input: S = "rabbbit", T = "rabbit"
    Output: 3
    Explanation:
    
    As shown below, there are 3 ways you can generate "rabbit" from S.
    (The caret symbol ^ means the chosen letters)
    
    rabbbit
    ^^^^ ^^
    rabbbit
    ^^ ^^^^
    rabbbit
    ^^^ ^^^
    Example 2:
    
    Input: S = "babgbag", T = "bag"
    Output: 5
    Explanation:
    
    As shown below, there are 5 ways you can generate "bag" from S.
    (The caret symbol ^ means the chosen letters)
    
    babgbag
    ^^ ^
    babgbag
    ^^    ^
    babgbag
    ^    ^^
    babgbag
      ^  ^^
    babgbag
        ^^^
"""
    width = len(S) + 1
    height = len(T) + 1
    temp = make_array(height, width)
    #    - b a b g b a g
    #  - 1 1 1 1 1 1 1 1
    #  b 0 1 1 2 2 3 3 3
    #  a 0 0 1 1 1 1 4 4
    #  g 0 0 0 0 1 1 1 5

    # init
    for i in range(width):
        temp[0][i] = 1
    for i in range(1, height):
        for j in range(1, width):
            temp[i][j] = temp[i][j - 1]
            if S[j - 1] == T[i - 1]:
                temp[i][j] += temp[i - 1][j - 1]
    return temp[height - 1][width - 1]


assert ans115("babgbag", "bag") == 5


def ans940(S):
    """ Given a string S, count the number of distinct, non-empty subsequences of S .
    Since the result may be large, return the answer modulo 10^9 + 7.
    Example 1:
    
    Input: "abc"
    Output: 7
    Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
    Example 2:
    
    Input: "aba"
    Output: 6 Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
    Example 3:
    
    Input: "aaa"
    Output: 3 Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
    Note:
    
    S contains only lowercase letters.
    1 <= S.length <= 2000
    """
    # 以字符i结尾的不同子序列个数
    temp = {k: 0 for k in "abcdefghijklmnopqrstuvwxyz"}
    # 上次刚刚以某个词结尾的
    last_temp = {k: 0 for k in "abcdefghijklmnopqrstuvwxyz"}
    mask = pow(10, 9) + 7
    # temp[i] += sum(temp) - temp[i] + 1
    #  对于aaa的情况，可以认为在当前sum(temp) - temp[i]个子串后面增加了aaa的情况。
    # 因此恰好满足这个递推公式

    for c in S:
        temp[c] += 1
        cur_sub_str = 0
        for k, v in temp.items():
            if k == c:
                continue
            cur_sub_str += v
            cur_sub_str %= mask
        temp[c] += cur_sub_str + last_temp[c]
        last_temp[c] += cur_sub_str
    return sum(temp.values())


assert ans940("aaa") == 3
assert ans940("aba") == 6
assert ans940("abc") == 7
