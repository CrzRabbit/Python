'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。


示例 1：

输入：n = 13
输出：6

示例 2：

输入：n = 0
输出：0

提示：

0 <= n <= 2 * 109
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def countDigitOne(self, n: int) -> int:
        i = 1
        ret = 0
        while i <= n:
            ret += (n // (i * 10)) * i + min(max(n % (i * 10) - i + 1, 0), i)
            i *= 10
        return ret
Solution().countDigitOne(1568)