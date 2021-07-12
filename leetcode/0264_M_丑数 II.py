'''
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。


示例 1：

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：

输入：n = 1
输出：1
解释：1 通常被视为丑数。

提示：

1 <= n <= 1690
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def nthUglyNumber(self, n: int) -> int:
        mem = set()
        mem.add(1)
        t = 2
        while mem.__len__() < n:
            if (t % 2 == 0 and t >> 1 in mem) or (t % 3 == 0 and t // 3 in mem) or (t % 5 == 0 and t // 5 in mem):
                mem.add(t)
            if mem.__len__() == n:
                return t
            t += 1
        return t - 1

Solution().nthUglyNumber(500)