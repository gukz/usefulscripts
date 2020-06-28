class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# TODO 找出树的最小深度
# 这种解法是错误的，需要额外设立全局变量保存最小值
def minDepth(node):
    if node is None:
        return 0
    left = minDepth(node.left)
    right = minDepth(node.right)
    return 1 + min(left, right)


def find3(nums):
    if len(nums) < 2:
        return None, None
    num1, num2 = nums[0], nums[1]
    index1, index2 = 1, 1
    for num in nums[2:]:
        if num == num1:
            index1 += 1
            continue
        if num == num2:
            index2 += 2
            continue
        index1 -= 1
        if index1 == 0:
            num1 = num
            index1 = 1
            continue
        index2 -= 1
        if index2 == 0:
            num2 = num
            index2 = 1
    if index1 + index2 < int(len(nums) * 2 / 3):
        return None, None
    return num1, num2


assert (3, 4) == find3([1, 2, 3, 3, 4, 4])


def depthSum(nList):
    """给一个嵌套的整数列表，按照深度加权取和"""

    def dfs(nodes, depth):
        curSum = 0
        for node in nodes:
            if type(node) == list:
                curSum += dfs(node, depth + 1)
            else:
                curSum += depth * node
        return curSum

    return dfs(nList, 1)


assert depthSum([1, 2, [3, 4, [5, 6, [7]]]]) == 78
