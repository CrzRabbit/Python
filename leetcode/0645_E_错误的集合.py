'''
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：
输入：nums = [1,2,2,4]
输出：[2,3]

示例 2：
输入：nums = [1,1]
输出：[1,2]

提示：

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findErrorNums(self, nums: List[int]) -> List[int]:
        self.len = len(nums)
        mem = [0 for i in range(self.len + 1)]
        xor = 0
        twice = None
        for i in range(self.len):
            xor ^= nums[i]
            mem[nums[i]] += 1
            if mem[nums[i]] == 2:
                twice = nums[i]
        for i in range(self.len):
            xor ^= (i + 1)
        return [twice, xor ^ twice]

nums = [1, 2, 2, 4]
Solution().findErrorNums(nums)