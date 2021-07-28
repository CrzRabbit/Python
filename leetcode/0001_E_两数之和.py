'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
'''
from typing import List

class Solution:
    '''
    排序 首尾之和大于target，尾部前移一位，小于target，首部后移
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(range(len(nums)), key=lambda key : nums[key])
        print(sorted_nums)
        head = 0
        tail = len(nums) - 1
        sumresult = nums[sorted_nums[head]] + nums[sorted_nums[tail]]
        while sumresult != target:
            if sumresult < target:
                head += 1
            if sumresult > target:
                tail -= 1
            if head > tail:
                return []
            sumresult = nums[sorted_nums[head]] + nums[sorted_nums[tail]]
        return [sorted_nums[head], sorted_nums[tail]]

so = Solution()
print(so.twoSum([2, 9, 8, 1, 6, 7], 3))