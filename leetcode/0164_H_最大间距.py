'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。

说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ret = 0
        for i in range(1, n):
            ret = max(ret, nums[i] - nums[i - 1])
        return ret

    '''
    基数排序
    '''
    @printTime()
    def _1maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        maxnum = max(nums)
        exp = 1
        while maxnum >= exp:
            temp = [0 for _ in range(n)]
            cnt = [0 for _ in range(10)]
            for i in range(n):
                index = (nums[i] // exp) % 10
                cnt[index] += 1
            for i in range(1, 10):
                cnt[i] += cnt[i - 1]
            for i in range(n - 1, -1, -1):
                index = (nums[i] // exp) % 10
                temp[cnt[index] - 1] = nums[i]
                cnt[index] -= 1
            exp *= 10
            nums = temp
        ret = 0
        for i in range(1, n):
            ret = max(ret, nums[i] - nums[i - 1])
        return ret

    '''
    桶排序
    '''
    @printTime()
    def _2maximumGap(self, nums: List[int]) -> int:
        pass

nums = [3,6,9,1,15]
Solution().maximumGap(nums)
Solution()._1maximumGap(nums)