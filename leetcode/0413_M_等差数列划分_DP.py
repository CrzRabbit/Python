'''
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

示例:
A = [1, 2, 3, 4]
返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def _1numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ret = 0
        self.len = len(nums)
        dp = [[0 for _ in range(self.len)] for _ in range(self.len)]
        for i in range(1, self.len - 1):
            j = i + 1
            temp = nums[i] * 2 - nums[j]
            if nums[i - 1] == temp:
                dp[i][j] = dp[i - 1][i] + 1
            ret += dp[i][j]
        return ret

    @printTime()
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ret = 0
        temp = 0
        self.len = len(nums)
        for i in range(1, self.len - 1):
            if nums[i - 1] == nums[i] * 2 - nums[i + 1]:
                temp = temp + 1
            else:
                temp = 0
            ret += temp
        return ret

nums = [1, 2, 3, 4, 5, 6]
Solution()._1numberOfArithmeticSlices(nums)
Solution().numberOfArithmeticSlices(nums)