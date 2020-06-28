def permute0(nums):
    nums = list(set(nums))
    if not nums:
        return []

    def dfs(n, nums, res):
        if n == len(nums):
            res.append(nums[:])
        for i in range(n, len(nums)):
            nums[n], nums[i] = nums[i], nums[n]
            dfs(n + 1, nums, res)
            nums[n], nums[i] = nums[i], nums[n]

    res = []

    #  print(nums)
    dfs(0, nums, res)
    return res
    #  print(res)
    #  print(nums)


assert len(permute0([1, 2, 3,])) == 6

# 2D找字母


def find_word_on_board(board, word):
    width, height = len(board), len(board[0])
    if not word or not board:
        return False

    def dfs(board, word, index, cur):
        if len(word) == index:
            return True
        x, y = cur
        board[x][y] = "*"
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            if (
                x + dx < width
                and y + dy < height
                and board[x + dx][y + dy] == word[index]
                and dfs(board, word, index + 1, (x + dx, y + dy))
            ):
                return True

        board[x][y] = word[index]
        return False

    for x in range(width):
        for y in range(height):
            if board[x][y] == word[0] and dfs(board, word, 1, (x, y)):
                return True
    return False


def solveSuduku(board):
    pass


def find_child_set(nums):
    if not nums:
        return []
    res = []
    nums.sort()

    def dfs(index, cur):
        # dfs 内的含义一定要表述清楚
        if index == len(nums):
            res.append(cur)
            return
        val = nums[index]
        amount = 1
        while index + amount < len(nums) and nums[index + amount] == val:
            amount += 1
        # dfs 内部一般只有一层循环
        for i in range(amount + 1):
            # 递归dfs时也需要一些条件
            dfs(index + amount, cur + [val] * i)

    # dfs 的入口一般是直接调用，也可能会需要满足一些特定条件才能调用
    dfs(0, list())
    return res


assert 32 == len(find_child_set([1, 2, 2, 2, 3, 4]))
