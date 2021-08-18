'''
一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。

比方说，如果我们有数对 (1,5) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8 。
给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：

nums 中每个元素 恰好 在 一个 数对中，且
最大数对和 的值 最小 。
请你在最优数对划分的方案下，返回最小的 最大数对和 。



示例 1：

输入：nums = [3,5,2,3]
输出：7
解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。
最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
示例 2：

输入：nums = [3,5,4,2,4,6]
输出：8
解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。


提示：

n == nums.length
2 <= n <= 105
n 是 偶数 。
1 <= nums[i] <= 105
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    nums排好序的情况下,前半部分表示为X0~Xn，后半部分表示为Y0~Yn
    有X0...X1X2...XnY0...Y1Y2...Yn
    如果此时X2 + Y1是最大值，那么就有：X2 + Y1 > X1 + Y2 -> X2 - X1 > Y2 - Y1
    交换X1 X2的位置, 新产生的值为X1 + Y1和X2 + Y2，其中X1 + Y1明显小于X2 + Y2，不考虑。直接考虑X2 + Y2和原来最大值：X2 + Y2 - (X2 + Y1) = Y2 - Y1 > 0
    可以看出最大值变大了，所以排序的情况下，首尾配对并向中间靠拢的情况才有最小的最大数对和
    '''
    @printTime()
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if (nums[i] + nums[j]) > ret:
                ret = nums[i] + nums[j]
            i += 1
            j -= 1
        return ret

nums = [3, 5, 4, 2, 4, 6]
Solution().minPairSum(nums)