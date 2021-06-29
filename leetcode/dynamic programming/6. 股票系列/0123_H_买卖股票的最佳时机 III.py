'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


示例 1:
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。

示例 4：
输入：prices = [1]
输出：0

提示：
1 <= prices.length <= 105
0 <= prices[i] <= 105
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    两次操作分别发生在[0, i], [i + 1:]，后面这一次可能没有，即i == len - 1的情况
    '''
    @printTime()
    def maxProfit(self, prices: List[int]) -> int:
        self.len = len(prices)
        mem = [0 for i in range(self.len)]
        min = prices[0]
        #正向遍历，计算[0, i]只交易一次的最大利润，保存为mem[i]
        for i in range(1, self.len):
            if prices[i] < min:
                min = prices[i]
            mem[i] = max(mem[i - 1], prices[i] - min)
        #dp表示[0, i], [i + 1:]总共的大小，当i == len - 1, 即第二次不存在, dp = mem[len - 1]
        dp = mem[self.len - 1]
        ret = dp
        mx = prices[self.len - 1]
        #反向遍历,计算[i + 1:]的最大利润，并结合之前的mem[i]找到最大值
        for i in range(self.len - 1, 1, -1):
            if prices[i] > mx:
                mx = prices[i]
            dp = mem[i - 1] + (mx - prices[i])
            if dp > ret:
                ret = dp
        return ret

prices = [1,2,3,4,5]
Solution().maxProfit(prices)