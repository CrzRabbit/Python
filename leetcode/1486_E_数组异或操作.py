'''
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。
'''
from functools import reduce

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(int.__xor__, [start + 2 * x for x in range(n)])

so = Solution()
print(so.xorOperation(5, 0))