'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。

提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        self.len1 = len(nums1)
        self.len2 = len(nums2)
        ret = 0
        dp = [[0 for _ in range(self.len2)] for _ in range(self.len1)]
        if nums1[0] == nums2[0]:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        if dp[0][0] > ret:
            ret = dp[0][0]
        for i in range(1, self.len2):
            if nums1[0] == nums2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
            if dp[0][i] > ret:
                ret = dp[0][i]
        for i in range(1, self.len1):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
            if dp[i][0] > ret:
                ret = dp[i][0]
        for i in range(1, self.len1):
            for j in range(1, self.len2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = 0
                if dp[i][j] > ret:
                    ret = dp[i][j]
        return ret

    @printTime()
    def _1findLength(self, nums1: List[int], nums2: List[int]) -> int:
        self.len1 = len(nums1)
        self.len2 = len(nums2)
        ret = 0
        dp = [[0 for _ in range(self.len2 + 1)] for _ in range(self.len1 + 1)]
        dp[0][0] = 0
        for i in range(1, self.len1 + 1):
            for j in range(1, self.len2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = 0
                if dp[i][j] > ret:
                    ret = dp[i][j]
        return ret

nums1 = [1,0,0,0,1]
nums2 = [1,0,0,1,1]
Solution().findLength(nums1, nums2)
Solution()._1findLength(nums1, nums2)