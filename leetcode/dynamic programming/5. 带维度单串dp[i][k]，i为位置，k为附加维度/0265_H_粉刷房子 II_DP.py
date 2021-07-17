'''
假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

注意：

所有花费均为正整数。

示例：

输入: [[1,5,3],[2,9,4]]
输出: 5
解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5;
     或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
进阶：
您能否在 O(nk) 的时间复杂度下解决此问题？
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def minCostII(self, costs: List[List[int]]) -> int:
        self.len = len(costs)
        self.k = len(costs[0])
        dp = [[0 for _ in range(self.k)] for _ in range(self.len)]
        dp[0] = costs[0]
        min1 = None
        min2 = None
        for i in range(self.k):
            if min1 is None and min2 is None:
                min1 = i
            elif min2 is None:
                if dp[0][i] <= dp[0][min1]:
                    min2 = min1
                    min1 = i
                else:
                    min2 = i
            else:
                if dp[0][i] <= dp[0][min1]:
                    min2 = min1
                    min1 = i
                elif dp[0][i] < dp[0][min2]:
                    min2 = i
        for i in range(1, self.len):
            t1 = None
            t2 = None
            for j in range(self.k):
                if j != min1:
                    dp[i][j] = costs[i][j] + dp[i - 1][min1]
                else:
                    dp[i][j] = costs[i][j] + dp[i - 1][min2]
                if t1 is None and t2 is None:
                    t1 = j
                elif t2 is None:
                    if dp[i][j] <= dp[i][t1]:
                        t2 = t1
                        t1 = j
                    else:
                        t2 = j
                else:
                    if dp[i][j] <= dp[i][t1]:
                        t2 = t1
                        t1 = j
                    elif dp[i][j] < dp[i][t2]:
                        t2 = j
            min1 = t1
            min2 = t2
        return dp[self.len - 1][min1]

costs = [[1,5,3],[2,9,4]]
Solution().minCostII(costs)