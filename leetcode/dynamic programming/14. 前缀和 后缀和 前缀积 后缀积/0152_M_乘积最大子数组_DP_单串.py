'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        ml = nums[0]
        ret = [[0, 0] for i in range(l)]
        if nums[0] >= 0:
            ret[0][1] = nums[0]
        else:
            ret[0][0] = nums[0]
        for i in range(1, l):
            if nums[i] > 0:
                if ret[i - 1][1] > 0:
                    ret[i][1] = ret[i - 1][1] * nums[i]
                else:
                    ret[i][1] = nums[i]
                if ret[i - 1][0] < 0:
                    ret[i][0] = ret[i - 1][0] * nums[i]
            if nums[i] < 0:
                if ret[i - 1][0] < 0:
                    ret[i][1] = ret[i - 1][0] * nums[i]
                if ret[i - 1][1] > 0:
                    ret[i][0] = ret[i - 1][1] * nums[i]
                else:
                    ret[i][0] = nums[i]
            if max(ret[i]) > ml:
                ml = max(ret[i])
        return ml

nums = [2,-5,-2,-4,3]
so = Solution()
so.maxProduct(nums)