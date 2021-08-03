'''
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。



示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：

输入：nums = [1,2,3,4]
输出：0

示例 3：

输入：nums = [1]
输出：0


提示：

1 <= nums.length <= 104
-105 <= nums[i] <= 105
'''
import bisect
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = []
        left = None
        right = None
        for i, num in enumerate(nums):
            br = bisect.bisect_right(temp, num)
            if br != temp.__len__():
                if left is None or br < left:
                    left = br
                right = i + 1
            bisect.insort(temp, num)
        return right - left if left is not None else 0
    '''
    leetcode 超过100%范例
    '''
    @printTime()
    def _1findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        left = n-1
        min_nums = nums[-1]
        for j in range(n-1, -1, -1):
            if nums[j] <= min_nums:
                min_nums = nums[j]
            else:
                left = j
        right = 0
        max_nums = nums[0]
        for i in range(n):
            if nums[i] >= max_nums:
                max_nums = nums[i]
            else:
                right = i
        return max(right - left + 1, 0)

nums = [1,3,5,4,2] * 2000
Solution().findUnsortedSubarray(nums)
Solution()._1findUnsortedSubarray(nums)