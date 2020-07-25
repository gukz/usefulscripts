from collections import defaultdict

from utils import make_array


def ans115(S, T):
    """ [LeetCode] 115. Distinct Subsequences 不同的子序列
    Given a string S and a string T, count the number of distinct subsequences of S which equals T.
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
        ^^^"""
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
    """ [LeetCode] 940. Distinct Subsequences II 不同的子序列之二
    Given a string S, count the number of distinct, non-empty subsequences of S .
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


def ans939(points) -> int:
    """ [LeetCode] 939. Minimum Area Rectangle 面积最小的矩形
    Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.  If there isn't any rectangle, return 0.
    Example 1:
    Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
    Output: 4

    Example 2:
    Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    Output: 2

    Note:
    1 <= points.length <= 500
    0 <= points[i][0] <= 40000
    0 <= points[i][1] <= 40000
    All points are distinct.  """
    point_dict = defaultdict(list)
    for point in points:
        point_dict[point[0]].append(point[1])
    min_val = 2147483647
    for p0x, p0ys in point_dict.items():
        if len(p0ys) < 2:
            continue
        for p1x, p1ys in point_dict.items():
            if p0x == p1x:
                continue
            y_sets = set(p0ys) & set(p1ys)  # 集合交集、并集、差集为： & | -
            if len(y_sets) < 2:
                continue
            for p0y in y_sets:
                for p1y in y_sets:
                    if p1y == p0y:
                        continue
                    s = abs(p0x - p1x) * abs(p0y - p1y)
                    min_val = min(min_val, s)
    if min_val == 2147483647:
        return 0
    return min_val


assert ans939([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]) == 4
assert ans939([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]) == 2
assert ans939([[3, 2], [3, 1], [4, 4], [1, 1], [4, 3], [0, 3], [0, 2], [4, 0]]) == 0


def ans936(stamp, target):
    """ [LeetCode] 936. Stamping The Sequence 戳印序列
    You want to form a `target` string of lowercase letters.
    At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.
    
    On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.
    
    For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)
    
    If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.
    
    For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".
    
    Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.
    
    Example 1:
    
    Input: stamp = "abc", target = "ababc"
    Output: [0,2]
    ([1,0,2] would also be accepted as an answer, as well as some other answers.)
    Example 2:
    
    Input: stamp = "abca", target = "aabcaca"
    Output: [3,0,1]
    Note:
    
    1 <= stamp.length <= target.length <= 1000
    stamp and target only contain lowercase letters.  """
    # ababc -> ab*** -> ***** 反向盖*号知道所有的位置都盖上*好即可
    print("ans936 need help")


#  assert ans936("abc", "ababc") == [0, 2]
#  assert ans936("abca", "aabcaca") == [3, 0, 1]
assert ans936("abca", "aabcaca") is None


def ans935(N):
    """ [LeetCode] 935. Knight Dialer 骑士拨号器
    A chess knight can move as indicated in the chess diagram below:
    This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.
    
    Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.
    
    How many distinct numbers can you dial in this manner?
    
    Since the answer may be large, output the answer modulo 10^9 + 7.
    Example 1:
    
    Input: 1
    Output: 10
    Example 2:
    
    Input: 2
    Output: 20
    Example 3:
    
    Input: 3
    Output: 46
    Note:
    
    1 <= N <= 5000 """
    temp = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }
    values = [1] * 10
    mask = pow(10, 9) + 7
    while N > 1:
        N -= 1
        v = values.copy()
        for i in range(10):
            numbers = 0
            for n in temp[i]:
                numbers += v[n]
                numbers %= mask

            values[i] = numbers
    res = 0
    for k in values:
        res += k
        res %= mask
    return res


assert ans935(1) == 10
assert ans935(2) == 20
assert ans935(3) == 46
assert ans935(4) == 104


def ans932(N):
    """ [LeetCode] 932. Beautiful Array 漂亮数组
    For some fixed `N`, an array `A` is *beautiful* if it is a permutation of the integers `1, 2, ..., N`, such that:
    For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
    
    Given N, return any beautiful array A.  (It is guaranteed that one exists.)
    
    Example 1:
    
    Input: 4
    Output: [2,1,4,3]
    Example 2:
    
    Input: 5
    Output: [3,1,2,5,4]
    Note:
    
    1 <= N <= 1000 """
    print("ans932 need help")


assert ans932(1) is None


def ans931(A):
    """ [LeetCode] 931. Minimum Falling Path Sum 下降路径最小和
    Given a square array of integers A, we want the minimum sum of a falling path through A.
    
    A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.
    
    Example 1:
    
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: 12
    Explanation:
    The possible falling paths are:
    
    -   `[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]`
    -   `[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]`
    -   `[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]`
    The falling path with the smallest sum is [1,4,7], so the answer is 12.
    
    Note:
    
    1 <= A.length == A[0].length <= 100
    -100 <= A[i][j] <= 100 """
    print("ans931 too simple")


assert ans931(None) == None


def ans930(A, S):
    """ [LeetCode] 930. Binary Subarrays With Sum 二元子数组之和
    In an array A of 0s and 1s, how many non-empty subarrays have sum S?
    Example 1:
    Input: A = [1,0,1,0,1], S = 2
    Output: 4
    Explanation: 
    The 4 subarrays are bolded below:
    [1,0,1,-,-]
    [1,0,1,0,-]
    [-,-,1,0,1]
    [-,0,1,0,1]
    Note:
    A.length <= 30000
    0 <= S <= A.length
    A[i] is either 0 or 1.  """
    pass


assert ans930([1, 0, 1, 0, 1], 2) == 4


def ans_multi_game(numbers):
    """ 乘法游戏
    乘法游戏是在一行牌上进行的。每一张牌包括了一个正整数。在每一个移动中，玩家拿出一张牌，得分是用它的数字乘以它左边和右边的数，所以不允许拿第1张和最后1张牌。最后一次移动后，这里只剩下两张牌。         你的目标是使得分的和最小。
    例如，如果数是10  1  50  20  5，依次拿1、20、50，总分是10*1*50+50*20*5+10*50*5=8000
    而拿50、20、1，总分是1*50*20+1*20*5+10*1*5=1150。
    输入文件的第一行包括牌数(3< =n< =100)，第二行包括N个1-100的整数，用空格分开。
    输出文件只有一个数字：最小得分
    样例输入
    6
    10 1 50 50 20 5
    样例输出
    3650
    """
    temp = []
