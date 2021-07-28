'''
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。


示例 1：

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。

示例 2：

输入：matrix = []
输出：0

示例 3：

输入：matrix = [["0"]]
输出：0

示例 4：

输入：matrix = [["1"]]
输出：1

示例 5：

输入：matrix = [["0","0"]]
输出：0

提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
'''
import heapq
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        len1 = len(matrix)
        if len1 == 0:
            return 0
        len2 = len(matrix[0])
        if len2 == 0:
            return 0
        dp = [[[0, 0] for _ in range(len2)] for _ in range(len1)]
        dp[0][0] = [1, 1] if matrix[0][0] == '1' else [0, 0]
        ret = dp[0][0][0] * dp[0][0][1]
        for i in range(1, len1):
            dp[i][0] = [dp[i - 1][0][0] + 1, 1] if matrix[i][0] == '1' else [0, 0]
            ret = max(ret, dp[i][0][0])
        for j in range(1, len2):
            dp[0][j] = [1, dp[0][j - 1][1] + 1] if matrix[0][j] == '1' else [0, 0]
            ret = max(ret, dp[0][j][1])
        for i in range(1, len1):
            for j in range(1, len2):
                if matrix[i][j] == '0':
                    dp[i][j] = [0, 0]
                else:
                    dp[i][j] = [dp[i - 1][j][0] + 1, dp[i][j - 1][1] + 1]
                temp = dp[i][j][1]
                for k in range(i, i - dp[i][j][0], -1):
                    temp = min(temp, dp[k][j][1])
                    ret = max(ret, (i + 1 - k) * temp)
        return ret

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Solution().maximalRectangle(matrix)