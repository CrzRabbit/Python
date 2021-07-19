'''
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        ret = sum
        for i in range(1, len(nums)):
            sum = sum + nums[i] if sum >= 0 else nums[i]
            if ret == None or sum > ret:
                ret = sum
        return ret

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Solution().maxSubArray(nums)