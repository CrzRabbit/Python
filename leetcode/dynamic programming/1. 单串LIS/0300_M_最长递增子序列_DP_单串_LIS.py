'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''
from typing import List


class Solution:
    '''
    动态规划
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        ret = 1
        l = len(nums)
        temp = [1 for i in range(l)]
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    temp[i] = max(temp[i], temp[j] + 1)
            if temp[i] > ret:
                ret = temp[i]
        return ret

nums = [1,3,6,7,9,4,10,5,6]
so = Solution()
print(so.lengthOfLIS(nums))