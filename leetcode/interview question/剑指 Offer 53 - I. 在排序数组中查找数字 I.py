'''
统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0


限制：

0 <= 数组长度 <= 50000
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def search(self, nums: List[int], target: int) -> int:
        self.len = len(nums)
        if self.len == 0:
            return 0
        left = 0
        right = self.len - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        t1 = left
        left = t1
        right = self.len - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return (left - t1 + 1) if nums[left] == target else left - t1

nums = [4,5,5]
target = 5
Solution().search(nums, target)