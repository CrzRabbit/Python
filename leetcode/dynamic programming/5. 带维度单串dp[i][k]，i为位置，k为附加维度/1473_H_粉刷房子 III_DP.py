'''
在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不可以被重新涂色。

我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）

给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：

houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。

示例 1：
输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：9
解释：房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。

示例 2：
输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：11
解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。

示例 3：
输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
输出：

示例 4：
输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
输出：-1
解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。

提示：
m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    自顶向下(未完成)
    '''
    @printTime()
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.len = len(houses)
        self.len1 = len(cost[0])
        lim = [0 for _ in range(self.len)]
        lim[0] = 1
        temp = None
        mem1 = {}
        mem2 = {}
        if houses[0] != 0:
            temp = 0
        for i in range(1, self.len):
            lim[i] = 1
            if temp is not None:
                lim[i] = lim[temp]
                if houses[i] != houses[temp] and houses[i] != 0:
                    lim[i] += 1
            if houses[i] != 0:
                temp = i
        if lim[-1] > target:
            return - 1
        def getCost(left, right):
            if (left, right) in mem2:
                return mem2[(left, right)]
            temp = None
            al = 0
            for i in range(left, right + 1):
                if houses[i] != 0:
                    al += cost[i][houses[i] - 1]
                    temp = houses[i]
            if temp is not None:
                ret = sum(cost[i][temp - 1] for i in range(left, right + 1)) - al
            else:
                ret = min(sum(cost[i][j] for i in range(left, right + 1)) for j in range(n))
            mem2[(left, right)] = ret
            return ret
        def dp(n, k):
            if k == 1:
                ret = getCost(0, n)
            elif n + 1 < k:
                ret = 0
            else:
                if (n, k) in mem1:
                   return mem1[(n, k)]
                ret = dp(n - 1, k - 1) + getCost(n, n)
                for i in range(n - 1, 0, -1):
                    if lim[n] == lim[i]:
                        temp = dp(i - 1, k - 1) + getCost(i, n)
                        if temp < ret:
                            ret = temp
                    else:
                        break
            mem1[(n, k)] = ret
            return ret
        ret = dp(m - 1, target)
        print(mem1)
        print(mem2)
        return ret
    '''
    自底向上
    '''
    @printTime()
    def _1minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.len = len(houses)
        #三维分别是房子，颜色，街区数，默认值为-1，dp[i][j][k]表示将第i个房子刷为第j种颜色并且(0~i)形成k个街区的最小花费
        dp = [[[-1 for _ in range(target)] for _ in range(n)] for _ in range(m)]
        #对于第一个房子，只能作为一个街区
        if houses[0] == 0:
            #任选颜色的第一个房子颜色维度上就是第一个房子在该颜色的花费
            for i in range(n):
                #第一个房子刷为第i种颜色形成一个街区
                dp[0][i][0] = cost[0][i]
        #已经有颜色的话该颜色维度上为0，其它都是-1
        else:
            dp[0][houses[0] - 1][0] = 0
        #对于（0 ~ i）的房子
        for i in range(1, self.len):
            #颜色可以任选的话
            if houses[i] == 0:
                #对于每一种颜色
                for j in range(n):
                    #一个街区的花费为之前的所有房子都是当前房子颜色的花费加上当前房子的花费，当前房子需要刷
                    dp[i][j][0] = (dp[i - 1][j][0] + cost[i][j]) if dp[i - 1][j][0] != -1 else -1
                    #多个街区的情况分为两种，并取最小值
                    for k in range(1, target if i + 1 > target else i + 1):
                        #第一种是当前房子和前一个房子是一种颜色
                        temp = dp[i - 1][j][k] if dp[i - 1][j][k] != -1 else None
                        #第二种是当前房子独立作为一个街区，和前一个房子颜色不同，需要遍历前一个房子可能的颜色来寻找最小值
                        for j1 in range(n):
                            if j1 != j and dp[i - 1][j1][k - 1] != -1 and (temp is None or dp[i - 1][j1][k - 1] < temp):
                                temp = dp[i - 1][j1][k - 1]
                        if temp is not None:
                            dp[i][j][k] = temp + cost[i][j]
            #已经有颜色的话
            else:
                #到当前房子为止总共一个街区的花费为之前的所有房子都是当前房子颜色的花费，当前房子已经有颜色了不需要再刷
                dp[i][houses[i] - 1][0] = dp[i - 1][houses[i] - 1][0]
                #多个街区的情况分为两种，并取最小值
                for k in range(1, target if i + 1 > target else i + 1):
                    #第一种是当前房子和前一个房子是一种颜色
                    temp = dp[i - 1][houses[i] - 1][k] if dp[i - 1][houses[i] - 1][k] != -1 else None
                    #第二种是当前房子独立作为一个街区，和前一个房子颜色不同，需要遍历前一个房子可能的颜色来寻找最小值
                    for j in range(n):
                        if j != houses[i] - 1 and dp[i - 1][j][k - 1] != -1 and (temp is None or dp[i - 1][j][k - 1] < temp):
                            temp = dp[i - 1][j][k - 1]
                    if temp is not None:
                        dp[i][houses[i] - 1][k] = temp
        #计算target个街区的最小值
        if houses[self.len - 1] == 0:
            ret = dp[self.len - 1][0][target - 1]
            for j in range(1, n):
                if j != houses[self.len - 1] and dp[self.len - 1][j][target - 1] != -1 and (ret == -1 or ret > dp[self.len - 1][j][target - 1]):
                    ret = dp[self.len - 1][j][target - 1]
        else:
            ret = dp[self.len - 1][houses[self.len - 1] - 1][target - 1]
        return ret

houses = [2,3,0]
cost = [[5,2,3],[3,4,1],[1,2,1]]
m = 3
n = 3
target = 3
Solution().minCost(houses, cost, m, n, target)
Solution()._1minCost(houses, cost, m, n, target)