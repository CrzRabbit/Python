'''
集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。

有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

示例 1：
输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
输出：2
解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。

示例 2：
输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
输出：7
解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。

提示：
1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
'''
import bisect
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        ans = 0
        if minProfit == 0:
            ans += 1
        mem = [(0, 0, 1)]
        for i in range(len(profit)):
            temp = {}
            br = bisect.bisect_left(mem, (n - group[i] + 1, 0, 0))
            for j in range(br):
                t1 = group[i] + mem[j][0]
                t2 = profit[i] + mem[j][1]
                if t1 < n:
                    if (t1, t2) not in temp:
                        temp[(t1, t2)] = 0
                    temp[(t1, t2)] += mem[j][2]
                if t1 <= n and t2 >= minProfit:
                    ans += mem[j][2]
            for k in temp.keys():
                mem.append((k[0], k[1], temp[k]))
            mem.sort()
        return ans % mod

    '''
    DP
    '''
    @printTime()
    def _1profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        pass

n = 100
minProfit = 100
group = [2,5,36,2,5,5,14,1,12,1,14,15,1,1,27,13,6,59,6,1,7,1,2,7,6,1,6,1,3,1,2,11,3,39,21,20,1,27,26,22,11,17,3,2,4,5,6,18,4,14,1,1,1,3,12,9,7,3,16,5,1,19,4,8,6,3,2,7,3,5,12,6,15,2,11,12,12,21,5,1,13,2,29,38,10,17,1,14,1,62,7,1,14,6,4,16,6,4,32,48]
profit = [21,4,9,12,5,8,8,5,14,18,43,24,3,0,20,9,0,24,4,0,0,7,3,13,6,5,19,6,3,14,9,5,5,6,4,7,20,2,13,0,1,19,4,0,11,9,6,15,15,7,1,25,17,4,4,3,43,46,82,15,12,4,1,8,24,3,15,3,6,3,0,8,10,8,10,1,21,13,10,28,11,27,17,1,13,10,11,4,36,26,4,2,2,2,10,0,11,5,22,6]
# Solution().profitableSchemes(n, minProfit, group, profit)
Solution()._1profitableSchemes(n, minProfit, group, profit)