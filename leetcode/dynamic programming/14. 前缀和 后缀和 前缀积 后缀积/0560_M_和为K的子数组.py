'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = {0: 1}
        ret = 0
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            t = temp - k
            if t in mem:
                ret += mem[t]
            if temp not in mem:
                mem[temp] = 0
            mem[temp] += 1
        return ret

nums = [1, 1, 1]
k = 2
Solution().subarraySum(nums, k)