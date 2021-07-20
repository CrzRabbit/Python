'''
给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长连续子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。


示例 1:

输入: nums = [1,-1,5,-2,3], k = 3
输出: 4
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
示例 2:

输入: nums = [-2,-1,2,1], k = 1
输出: 2
解释: 子数组 [-1, 2] 和等于 1，且长度最长。


提示：

1 <= nums.length <= 2 * 105
-104 <= nums[i] <= 104
-109 <= k <= 109

进阶:
你能使时间复杂度在 O(n) 内完成此题吗?
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    前缀和
    '''
    @printTime()
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mem = {0: 0}
        sum = 0
        ret = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in mem and i - mem[sum - k] + 1 > ret:
                ret = i - mem[sum - k] + 1
            if sum not in mem:
                mem[sum] = i + 1
        return ret

nums = [1,-1,5,-2,3]
k = 3
Solution().maxSubArrayLen(nums, k)