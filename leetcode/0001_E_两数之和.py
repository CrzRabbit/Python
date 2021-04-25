'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0

提示：
-231 <= x <= 231 - 1
'''
from typing import List

class Solution:
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