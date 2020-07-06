# 1504. Count Submatrices With All Ones
# https://leetcode.com/problems/count-submatrices-with-all-ones/
# 这一题的意思是在一个0，1矩阵里面，找出子矩阵，要求子矩阵所有元素都是1


class Solution1:
    # 遍历没有元素，暴力搜索。底层使用二分查找优化搜索效率 8秒+
    def get_sum(self, i1, j1, i2, j2):
        return (
            self.sum_mat[i2][j2]
            + self.sum_mat[i1][j1]
            - self.sum_mat[i1][j2]
            - self.sum_mat[i2][j1]
        )

    def numSubmat(self, mat: list[list[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        sum_mat = []
        for i in range(rows + 1):
            sum_mat.append([0] * (cols + 1))
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                val = sum_mat[i - 1][j - 1]
                for i1 in range(i - 1):
                    val += mat[i1][j - 1]
                for j1 in range(j - 1):
                    val += mat[i - 1][j1]
                sum_mat[i][j] = val + mat[i - 1][j - 1]

        # we build sum_mat successful
        self.sum_mat = sum_mat
        temp = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                i1, j1 = i - 1, j - 1
                for height in range(rows):
                    if i + height > rows:
                        break
                    if self.get_sum(i1, j1, i + height, j) != height + 1:
                        break
                    # while j + width <= cols:  # bin search
                    #    if self.get_sum(i1, j1, i+height, j+width) != (width+1) * (height+1):
                    #        break
                    #    width += 1
                    width = 0
                    left, right = 0, cols - j
                    while left <= right:
                        mid = (left + right + 1) // 2
                        if self.get_sum(i1, j1, i + height, j + mid) == (mid + 1) * (
                            height + 1
                        ):
                            left = mid
                            width = mid
                        else:
                            right = mid - 1
                        if right <= left + 1:
                            if self.get_sum(i1, j1, i + height, j + right) == (
                                right + 1
                            ) * (height + 1):
                                width = right
                            break
                    temp += width + 1
        return temp


class Solution2:
    # 动态规划
    def numSubmat(self, mat: list[list[int]]) -> int:
        pass
