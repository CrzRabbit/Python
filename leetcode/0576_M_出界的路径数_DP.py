'''
给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。

给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。


示例 1：

输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
输出：6

示例 2：

输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
输出：12

提示：

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        n, m = m, n
        mod = 10 ** 9 + 7
        dp = [[[0 for _ in range(maxMove)] for _ in range(m)] for _ in range(n)]
        if maxMove > 0:
            dp[startRow][startColumn][0] = 1
        for k in range(1, maxMove):
            for i in range(max(0, startRow - k), min(n, startRow + k + 1)):
                for j in range(max(0, startColumn - k), min(m, startColumn + k + 1)):
                    if i > 0:
                        dp[i][j][k] += dp[i - 1][j][k - 1]
                    if i < n - 1:
                        dp[i][j][k] += dp[i + 1][j][k - 1]
                    if j > 0:
                        dp[i][j][k] += dp[i][j - 1][k - 1]
                    if j < m - 1:
                        dp[i][j][k] += dp[i][j + 1][k - 1]
                    dp[i][j][k] %= mod
        cnt = 0
        for i in range(0, n):
            for k in range(maxMove):
                cnt += dp[i][0][k] + dp[i][m - 1][k]
        for j in range(0, m):
            for k in range(maxMove):
                cnt += dp[0][j][k] + dp[n - 1][j][k]
        return cnt % mod
m = 2
n = 2
maxMove = 0
startRow = 0
startColumn = 0
Solution().findPaths(m, n, maxMove, startRow, startColumn)