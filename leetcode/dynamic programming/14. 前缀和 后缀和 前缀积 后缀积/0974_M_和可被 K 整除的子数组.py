'''
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。


示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mem = {0: 1}
        count = 0
        sum = 0
        for n in nums:
            sum += n
            if sum % k in mem:
                count += mem[sum % k]
            else:
                mem[sum % k] = 0
            mem[sum % k] += 1
        return count

A = [4, 5, 0, -2, -3, 1]
K = 5
Solution().subarraysDivByK(A, K)