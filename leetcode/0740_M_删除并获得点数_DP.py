'''
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1：
输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。

示例 2：
输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        dp = [0 for _ in range(len(nums))]
        index = 0
        left = 0
        dp[index] = nums[0]
        for right in range(1, len(nums)):
            if nums[right] == nums[left]:
                dp[index] += nums[right]
            else:
                index += 1
                dp[index] = nums[right]
                if (nums[left] + 1) == nums[right] and index >= 2:
                    dp[index] += max(dp[:index - 1])
                elif (nums[left] + 1) != nums[right] and index > 0:
                    dp[index] += max(dp[:index])
                left = right
        return max(dp)

nums = [1,1,1,2,4,5,5,5,6]
so = Solution()
so.deleteAndEarn(nums)