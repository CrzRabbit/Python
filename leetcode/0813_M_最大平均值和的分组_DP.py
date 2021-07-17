'''
我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。

示例:
输入:
A = [9,1,2,3,9]
K = 3
输出: 20
解释:
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
说明:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
答案误差在 10^-6 内被视为是正确的。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        self.len = len(nums)
        mem = []
        sum = 0
        for i in range(self.len):
            sum += nums[i]
            mem.append(sum)
        dp = [[0 for _ in range(k)] for _ in range(self.len)]
        for i in range(self.len):
            for j in range(k):
                if j == 0:
                    dp[i][j] = max(dp[i][j], mem[i] / (i + 1))
                    continue
                for x in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (mem[i] - mem[x]) / (i - x))
        return dp[self.len - 1][k - 1]

nums = [1,2,3,4,5,6,7]
k = 4
Solution().largestSumOfAverages(nums, k)