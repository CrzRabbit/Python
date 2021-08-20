'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。


示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：

输入：nums = [1], k = 1
输出：[1]

示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：

输入：nums = [9,11], k = 2
输出：[11]

示例 5：

输入：nums = [4,-2], k = 2
输出：[4]

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
import collections
import heapq
import math
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    优先队列
    '''
    @printTime()
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        hq = []
        ret = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(hq, [-nums[i], i])
        ret.append(-hq[0][0])
        for i in range(k, n):
            heapq.heappush(hq, [-nums[i], i])
            while hq[0][1] <= i - k:
                heapq.heappop(hq)
            ret.append(-hq[0][0])
        return ret
    '''
    单调队列
    '''
    @printTime()
    def _1maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ret = []
        n = len(nums)
        dq = collections.deque()
        for i in range(k):
            while dq.__len__() and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
        ret.append(dq[0])
        for i in range(k, n):
            while dq.__len__() and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
            if dq[0] == nums[i - k]:
                dq.popleft()
            ret.append(dq[0])
        return ret

    '''
    稀疏表
    '''
    @printTime()
    def _2maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        class SparseTable:
            def __init__(self, table):
                self.n = len(table)
                self.m = math.ceil(math.log(self.n, 2))
                self.f = [[0 for i in range(self.m + 1)] for i in range(self.n + 1)]
                for i in range(1, self.n + 1):
                    self.f[i][0] = table[i - 1]
                for i in range(1, self.m + 1):
                    for j in range(1, self.n - (1 << i) + 2):
                        self.f[j][i] = max(self.f[j][i - 1], self.f[j + (1 << (i - 1))][i - 1])
                self.mem = [0 for i in range(self.n + 1)]
                for i in range(2, self.n + 1):
                    self.mem[i] = self.mem[i // 2] + 1

            def get(self, l, r):
                s = self.mem[r - l + 1]
                return max(self.f[l][s], self.f[r - (1 << s) + 1][s])
        st = SparseTable(nums)
        ret = []
        for i in range(len(nums) - k + 1):
            ret.append(st.get(i + 1, i + k))
        return ret

nums = [1,3,-1,-3,5,3,6,7]
k = 3
Solution().maxSlidingWindow(nums, k)
Solution()._1maxSlidingWindow(nums, k)
Solution()._2maxSlidingWindow(nums, k)