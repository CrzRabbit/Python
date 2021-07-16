'''
给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。

区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。



示例 1：
输入：nums = [-2,5,-1], lower = -2, upper = 2
输出：3
解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
示例 2：

输入：nums = [0], lower = 0, upper = 0
输出：1


提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
题目数据保证答案是一个 32 位 的整数
'''
from typing import List

from leetcode.tools.sortedcontainers import SortedList
from leetcode.tools.time import printTime


class Solution:
    '''
    线段树
    '''
    @printTime()
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pass

    '''
    有序链表
    '''
    @printTime()
    def _1countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        sl.add(0)
        sum = 0
        count = 0
        for n in nums:
            sum += n
            bl = sl.bisect_left(sum - upper)
            br = sl.bisect_right(sum - lower)
            count += br - bl
            sl.add(sum)
        return count

nums = [-2, 5, -1]
lower = -2
upper = 2
Solution().countRangeSum(nums, lower, upper)
Solution()._1countRangeSum(nums, lower, upper)