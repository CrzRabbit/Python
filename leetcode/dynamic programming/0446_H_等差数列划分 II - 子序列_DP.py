'''
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。

如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。


示例 1：

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

示例 2：

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。

提示：

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}
        for i, num in enumerate(nums):
            if num not in mem:
                mem[num] = []
            mem[num].append(i)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                t = nums[i] * 2 - nums[j]
                if t in mem:
                    for k in mem[t]:
                        if k < i:
                            dp[i][j] += 1 + dp[k][i]
                        else:
                            break
                count += dp[i][j]
        return count

nums = [7,7,7,7,7] * 100
Solution().numberOfArithmeticSlices(nums)