'''
数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。


示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5

示例 2：

输入：[3,2]
输出：-1
示例 3：

输入：[2,2,1,1,1,2,2]
输出：2
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 1
        temp = nums[0]
        MAGIC = len(nums) >> 1
        for i in range(1, len(nums)):
            if nums[i] == temp:
                count += 1
            else:
                temp = nums[i]
                count = 1
            if count > MAGIC:
                return temp
        if count > MAGIC:
            return temp
        return -1

nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
Solution().majorityElement(nums)