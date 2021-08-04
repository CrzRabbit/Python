'''
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
'''
import bisect
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                bl = bisect.bisect_left(nums, nums[i] + nums[j])
                if bl > j:
                    count += bl - (j + 1)
                    if bl == n:
                        for k in range(j + 1, n - 1):
                            count += n - k - 1
                        break
        return count

nums = [2, 2, 3, 4] * 250
Solution().triangleNumber(nums)