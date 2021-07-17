'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
import math
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    动态规划
    '''
    @printTime()
    def coinChange(self, coins: List[int], amount: int) -> int:
        ret = [-1 for i in range(amount + 1)]
        coins = sorted(coins)
        ret[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and ret[i - coin] >= 0:
                    if ret[i] < 0:
                        ret[i] = ret[i - coin] + 1
                    else:
                        ret[i] = min(ret[i], ret[i - coin] + 1)
                elif i - coin < 0:
                    break
        return ret[amount]
    '''
    dfs
    '''
    @printTime()
    def _1coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)
        self.minCount = float('inf')
        l = len(coins)
        def dfs(target, index, count):
            coin = coins[index]
            temp = target // coin
            if math.ceil(target / coin) + count >= self.minCount:
                return
            if target % coin == 0:
                self.minCount = temp + count
            if index == l - 1:
                return
            for i in range(temp, -1, -1):
                dfs(target - coin * i, index + 1, count + i)
        dfs(amount, 0, 0)
        return self.minCount if self.minCount != float('inf') else -1

so = Solution()
coins = [411,412,413,414,415,416,417,418,419,420,421,422]
so.coinChange(coins, 9864)
so._1coinChange(coins, 9864)
# coins = [1, 2, 5]
# amount = 115
# so.coinChange(coins, amount)
# so._1coinChange(coins, amount)