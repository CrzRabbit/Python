'''
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。

这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

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
    '''
    记忆化搜索
    '''
    @printTime()
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums
        nums += [1]
        n = len(nums)
        mem = {}
        def recursion(left, right):
            if (left, right) in mem:
                return mem[(left, right)]
            if left + 2 > right:
                ans = 0
            elif left + 2 == right:
                ans = nums[left] * nums[left + 1] * nums[right]
            else:
                ans = nums[left] * nums[left + 1] * nums[right] + recursion(left + 1, right)
                for i in range(left + 2, right):
                    ans = max(ans, nums[left] * nums[i] * nums[right] + recursion(left, i) + recursion(i, right))
            mem[(left, right)] = ans
            return ans
        recursion(0, n - 1)
        return mem[(0, n - 1)]

    '''
    记忆化搜索
    '''
    @printTime()
    def _1maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums
        nums += [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if j == i + 2:
                    dp[i][j] = nums[i] * nums[i + 1] * nums[i + 2]
                    continue
                dp[i][j] = nums[i] * nums[i + 1] * nums[j] + dp[i + 1][j]
                for k in range(i + 2, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
        return dp[0][-1]

nums = [3,1,5,8]
Solution().maxCoins(nums)
Solution()._1maxCoins(nums)