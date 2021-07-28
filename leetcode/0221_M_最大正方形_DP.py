'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。


示例 1：

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例 2：

输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：

输入：matrix = [["0"]]
输出：0

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        len1 = len(matrix)
        len2 = len(matrix[0])
        dp = [[0 for _ in range(len2)] for _ in range(len1)]
        dp[0][0] = 1 if matrix[0][0] == '1' else 0
        ret = dp[0][0]
        for i in range(1, len1):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            if dp[i][0] > ret:
                ret = dp[i][0]
        for j in range(1, len2):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            if dp[0][j] > ret:
                ret = dp[0][j]
        for i in range(1, len1):
            for j in range(1, len2):
                count = min(dp[i - 1][j], dp[i][j - 1])
                if matrix[i][j] == '1':
                    count += 1
                else:
                    count = 0
                if count > dp[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = count
                if dp[i][j] > ret:
                    ret = dp[i][j]
        return ret ** 2

matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
Solution().maximalSquare(matrix)