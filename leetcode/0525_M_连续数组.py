'''
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。

示例 2:
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

提示：
1 <= nums.length <= 105
nums[i] 不是 0 就是 1
'''
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ret = 0
        count0 = 0
        count1 = 0
        mem = dict()
        mem[0] = [0, 0]
        for num in nums:
            if num == 0:
                count0 += 1
            if num == 1:
                count1 += 1
            if mem.keys().__contains__(count0 - count1):
                print(mem, count0, count1)
                count = count0 + count1 - mem[count0 - count1][0] - mem[count0 - count1][1]
                if count > ret:
                    ret = count
            else:
                mem[count0 - count1] = [count0, count1]
        return ret

nums = [1, 1, 1, 0, 0, 0]
so = Solution()
print(so.findMaxLength(nums))