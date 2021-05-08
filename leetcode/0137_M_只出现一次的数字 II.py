'''
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

示例 1：
输入：nums = [2,2,3,2]
输出：3

示例 2：
输入：nums = [0,1,0,1,0,1,99]
输出：99
 

提示：
1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = {}
        for num in nums:
            if num not in ret:
                ret[num] = 1
            else:
                ret[num] += 1
        for k in ret.keys():
            if ret[k] == 1:
                return k
        return None

nums = [0,1,0,1,0,1,99]
so = Solution()
print(so.singleNumber(nums))