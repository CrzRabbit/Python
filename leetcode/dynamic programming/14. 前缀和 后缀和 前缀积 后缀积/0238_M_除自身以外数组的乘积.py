'''
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。


示例:

输入: [1,2,3,4]
输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mem = [0 for i in range(len(nums))]
        products = [0 for i in range(len(nums))]
        mem[0] = nums[0]
        for i in range(1, len(nums)):
            mem[i] = nums[i] * mem[i - 1]
        products[-1] = mem[-2]
        product = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            products[i] = product * mem[i - 1]
            product *= nums[i]
        products[0] = product
        return products

nums = [1,2,3,4]
Solution().productExceptSelf(nums)