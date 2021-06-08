'''
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

示例 2:
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
'''
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        ret = [1 for i in range(l)]
        ml = 0
        count = 0
        for i in range(l):
            if i == 0:
                ml = 1
                count = 1
                continue
            for j in range(i):
                if nums[i] > nums[j]:
                    ret[i] = max(ret[i], ret[j] + 1)
        return count

nums = [2,2,2,2,2]
so = Solution()
print(so.findNumberOfLIS(nums))