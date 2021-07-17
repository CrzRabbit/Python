'''
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:
输入: amount = 10, coins = [10]
输出: 1

注意:
你可以假设：
0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    动态规划
    '''
    @printTime()
    def change(self, amount: int, coins: List[int]) -> int:
        l = len(coins)
        ret = [0 for i in range(amount + 1)]
        ret[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                ret[i] = ret[i] + ret[i - coin]
        return ret[amount]
    '''
    dfs
    '''
    @printTime()
    def _1change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins, reverse=True)
        l = len(coins)
        self.minCoin = coins[l - 1]
        mem = {}
        def dfs(target, index):
            if (target, index) in mem:
                return mem[(target, index)]
            count = 0
            coin = coins[index]
            if target % coin == 0:
                count += 1
            if index == l - 1:
                return count
            for i in range(target // coin, -1, -1):
                temp = target - coin * i
                if temp >= self.minCoin:
                    count += dfs(temp, index + 1)
            mem[(target, index)] = count
            return count
        return dfs(amount, 0)

coins = [3,5,7,8,9,10,11]
#coins = [1, 2, 5]
so = Solution()
so.change(500, coins)
so._1change(500, coins)