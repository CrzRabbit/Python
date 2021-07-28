'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。


示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    自底向上
    '''
    @printTime()
    def maxProfit(self, prices: List[int]) -> int:
        self.len = len(prices)
        if self.len < 2:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(self.len)]
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        for i in range(1, self.len):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return max(dp[self.len - 1][0], dp[self.len - 1][1])

    '''
    自顶向下
    '''
    @printTime()
    def _1maxProfit(self, prices: List[int]) -> int:
        self.len = len(prices)
        self.max = 0
        mem1 = {}
        mem2 = [[0 for _ in range(self.len)] for _ in range(self.len)]
        '''
        mem2[i][j]表示在[i, j]区间交易一次所能获取到的最大利润
        '''
        for i in range(self.len - 1):
            min = prices[i]
            ret = 0
            for j in range(i + 1, self.len):
                temp = prices[j] - min
                if temp > ret:
                    ret = temp
                if prices[j] < min:
                    min = prices[j]
                mem2[i][j] = ret
                if mem2[i][j] > self.max:
                    self.max = mem2[i][j]
        def dp(n):
            if n < 1:
                ans = 0
            else:
                if n in mem1:
                    return mem1[n]
                ans = dp(n - 1)
                for i in range(n - 1, -1, -1):
                    temp = dp(i - 2) + mem2[i][n]
                    if temp > ans:
                        ans = temp
                    if mem2[i][n] == self.max:
                        break
            mem1[n] = ans
            return ans
        ret = dp(self.len - 1)
        return ret

prices = [1,2,3,0,2,1,4,5,6,23,1,5,6,3,7]
Solution().maxProfit(prices)
Solution()._1maxProfit(prices)