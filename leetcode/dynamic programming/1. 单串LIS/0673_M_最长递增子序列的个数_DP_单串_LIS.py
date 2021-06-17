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
        count = [1 for i in range(l)]
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    if ret[j] + 1 > ret[i]:
                        ret[i] = ret[j] + 1
                        count[i] = count[j]
                    elif ret[j] + 1 == ret[i]:
                        count[i] += count[j]
        ml = max(ret)
        return sum(c for i, c in enumerate(count) if ret[i] == ml)

nums = [2,2,2,2,2]
so = Solution()
print(so.findNumberOfLIS(nums))