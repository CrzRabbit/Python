'''
给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。

区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。



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
import bisect
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    线段树
    '''
    @printTime()
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        class SegmentTreeS:
            def __init__(self, data):
                self.n = len(data)
                self.tree = [0 for _ in range(self.n << 1)]
                self.tree[self.n:] = data
                for i in range(self.n - 1, 0, -1):
                    self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]

            def supdate(self, index, val):
                index += self.n
                self.tree[index] += val
                while index > 0:
                    left = index
                    right = index
                    if left % 2 == 1:
                        left -= 1
                    else:
                        right += 1
                    index >>= 1
                    self.tree[index] = self.tree[left] + self.tree[right]

            def update(self, l, r, val):
                for i in range(l, r + 1):
                    self.supdate(i, val)

            def query(self, left, right):
                left += self.n
                right += self.n
                sum = 0
                while left <= right:
                    if left % 2 == 1:
                        sum += self.tree[left]
                        left += 1
                    if right % 2 == 0:
                        sum += self.tree[right]
                        right -= 1
                    left >>= 1
                    right >>= 1
                return sum
        n = len(nums)
        count = 0
        st = SegmentTreeS(nums)
        for i in range(0, n):
            for j in range(i, n):
                t = st.query(i, j)
                if t >= lower and t <= upper:
                    count += 1
        return count

    '''
    有序链表
    '''
    @printTime()
    def _1countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = [0]
        sum = 0
        count = 0
        for n in nums:
            sum += n
            bl = bisect.bisect_left(sl, sum - upper)
            br = bisect.bisect_right(sl, sum - lower)
            count += br - bl
            bisect.insort(sl, sum)
        return count

nums = [-2, 5, -1] * 100000
lower = -2
upper = 2
#Solution().countRangeSum(nums, lower, upper)
Solution()._1countRangeSum(nums, lower, upper)