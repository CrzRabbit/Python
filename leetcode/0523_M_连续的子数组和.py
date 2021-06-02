'''
给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。

示例 1：
输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。

示例 2：
输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。

示例 3：
输入：nums = [23,2,6,4,7], k = 13
输出：false

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
'''
from typing import List
from leetcode.tools.time import *

class Solution:
    def _1checkSubarraySum(self, nums: List[int], k: int) -> bool:
        temp = [0]
        sum = 0
        for num in nums:
            sum += num
            temp.append(sum)
        for i in range(len(temp) - 2):
            for j in range(i + 2, len(temp)):
                if (temp[j] - temp[i]) % k == 0:
                    return True
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur = 0
        sum = 0
        mem = {}
        mem[0] = []
        for j in range(len(nums)):
            num = nums[j]
            sum += num
            if sum >= 0 and sum < k:
                mem[cur].append(sum)
            elif sum >= cur * k and sum < (cur + 1) * k:
                if mem[cur].__contains__(sum) and (j >= 1 and (num != k or nums[j - 1] == 0)):
                    return True
                else:
                    mem[cur].append(sum)
            else:
                last = cur
                while sum >= (cur + 1) * k:
                    cur += 1
                mem[cur] = [sum]
                if sum == cur * k and (j >= 1 and (num != k or nums[j - 1] == 0)):
                    return True
                for i in range(len(mem[last])):
                    t1 = mem[last][i] + (cur - last) * k
                    mem[cur].append(t1)
                    if sum == t1 and (j >= 1 and (num != k or nums[j - 1] == 0)):
                        return True
        return False

nums = [0, 0]
so = Solution()
print(so._1checkSubarraySum(nums, 1))
print(so.checkSubarraySum(nums, 1))