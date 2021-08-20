'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。


示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
import datetime
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    并查集
    '''
    @printTime()
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        nums.sort()
        self.ret = 1
        fa = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(index):
            if index == fa[index]:
                return index
            fa[index] = find(fa[index])
            return fa[index]
        def merge(i, j):
            fi = find(i)
            fj = find(j)
            if rank[fi] >= rank[fj]:
                fa[fj] = fi
                rank[fi] += rank[fj]
                self.ret = max(self.ret, rank[fi])
            else:
                fa[fi] = fj
                rank[fj] += rank[fi]
                self.ret = max(self.ret, rank[fj])
        '''
        去重
        '''
        index = 1
        j = 1
        while j < n:
            if nums[j] != nums[j - 1]:
                nums[index] = nums[j]
                if abs(nums[index] - nums[index - 1]) == 1:
                    merge(index - 1, index)
                index += 1
            j += 1
        return self.ret

    @printTime()
    def _1longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        nums.sort()
        ret = 1
        temp = 0
        index = 1
        j = 1
        while j < n:
            if nums[j] != nums[j - 1]:
                nums[index] = nums[j]
                if nums[index] - nums[index - 1] > 1:
                    ret = max(ret, index - temp)
                    temp = index
                index += 1
            j += 1
        ret = max(ret, index - temp)
        return ret

nums = []
Solution().longestConsecutive(nums)
Solution()._1longestConsecutive(nums)