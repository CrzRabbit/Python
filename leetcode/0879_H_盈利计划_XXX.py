'''
集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。

有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

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
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    递归
    '''
    @printTime()
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.count = 0
        self.len = len(profit)
        mem = {}
        def recursion(people, pro, index):
            if(people, pro, index) in mem:
                return mem[(people, pro, index)]
            count = 0
            if self.len == index:
                return count
            recursion(people, pro, index + 1)
            if people + group[index] <= n:
                if pro + profit[index] >= minProfit:
                    count += 1
                count += recursion(people + group[index], pro + profit[index], index + 1)
            mem[(people, pro, index)] = count
            return count
        self.count = recursion(0, 0, 0)
        if minProfit == 0:
            self.count += 1
        return self.count % (10 ** 9 + 7)

    @printTime()
    def _1profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.count = 0
        self.len = len(profit)
        def recursion(people, pro, index):
            if self.len == index:
                return
            recursion(people, pro, index + 1)
            if people + group[index] <= n:
                if pro + profit[index] >= minProfit:
                    self.count += 1
                recursion(people + group[index], pro + profit[index], index + 1)
        recursion(0, 0, 0)
        if minProfit == 0:
            self.count += 1
        return self.count % (10 ** 9 + 7)

    '''
    DP
    '''
    @printTime()
    def _2profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.count = 0
        self.len = len(profit)
        self.magic = (10 ** 9) + 7
        dp = [[] for _ in range(self.len)]
        count = 0
        while True:
            temp = count * group[0]
            if temp <= n:
                dp[0].append([n - temp, count * profit[0]])
            else:
                break
            count += 1
        for i in range(1, self.len):
            print(i)
            for case in dp[i - 1]:
                count = 0
                while True:
                    temp = count * group[i]
                    if temp <= case[0]:
                        dp[i].append([case[0] - temp, case[1] + count * profit[i]])
                    else:
                        break
                    count += 1

        print(dp)

# Solution().profitableSchemes(10, 5, [2,3,5], [6, 7, 8])
# Solution()._1profitableSchemes(10, 5, [2,3,5], [6, 7, 8])
group = [82,7,18,34,1,3,83,56,50,34,39,38,76,92,71,2,6,74,1,82,22,73,88,98,6,71,6,26,100,75,57,88,43,16,22,89,7,9,78,97,22,87,34,81,74,56,49,94,87,71,59,6,20,66,64,37,2,42,30,87,73,16,39,87,28,9,95,78,43,59,87,78,2,93,7,22,21,59,68,67,65,63,78,20,82,35,86]
profit = [45,57,38,64,52,92,31,57,31,52,3,12,93,8,11,60,55,92,42,27,40,10,77,53,8,34,87,39,8,35,28,70,32,97,88,54,82,54,54,10,78,23,82,52,10,49,8,36,9,52,81,26,5,2,30,39,89,62,39,100,67,33,86,22,49,15,94,59,47,41,45,17,99,87,77,48,22,77,82,85,97,66,3,38,49,60,66]
#Solution()._1profitableSchemes(95, 53, group, profit)
Solution()._2profitableSchemes(95, 53, group, profit)