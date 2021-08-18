'''
给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。

丑数是可以被 a 或 b 或 c 整除的 正整数 。


示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。

示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。

示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。

示例 4：

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984.

提示：

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
本题结果在 [1, 2 * 10^9] 的范围内
'''
from math import gcd

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        self.len = 3
        def lcm(num1, num2):
            return (num1 * num2) // gcd(num1, num2)
        lab = lcm(a, b)
        lac = lcm(a, c)
        lbc = lcm(b, c)
        labc = lcm(lab, c)
        left = min(a, b, c)
        right = min(left * n, 2 * (10 ** 9) + 1)
        while left < right:
            mid = (right + left) >> 1
            temp = mid // a + mid // b + mid // c - mid // lab - mid // lac - mid // lbc + mid // labc
            if temp < n:
                left = mid + 1
            else:
                right = mid
        return left

Solution().nthUglyNumber(4, 2, 3, 4)