'''
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 

这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。



示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：

输入：nums = [1,5]
输出：10

提示：

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    pass
        return dp[0][-1]

    '''
    递归
    '''
    @printTime()
    def _1maxCoins(self, nums: List[int]) -> int:
        self.ret = 0
        def recursion(nums, coins):
            if len(nums) == 2:
                ans = (min(nums) + 1) * max(nums) + coins
                self.ret = max(self.ret, ans)
                return
            for i in range(len(nums)):
                temp = 1
                if i - 1 >= 0:
                    temp *= nums[i - 1]
                temp *= nums[i]
                if i + 1 <= len(nums) - 1:
                    temp *= nums[i + 1]
                recursion(nums[:i] + nums[i + 1:], temp + coins)
        recursion(nums, 0)
        return self.ret

nums = [3,1,5,8]
Solution().maxCoins(nums)
Solution()._1maxCoins(nums)
'''
1 3
1 * 3 + 3 = 6

3 5
3 * 5 + 5 = 20

1 3 5
1 * 3 * 5 + 1 * 5 + 5 = 25
'''