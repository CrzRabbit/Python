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

    @printTime()
    def _1nthUglyNumber(self, n: int) -> int:
        mem = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        while mem.__len__() < n:
            t1 = mem[index2] * 2
            t2 = mem[index3] * 3
            t3 = mem[index5] * 5
            t4 = min(t1, t2, t3)
            if t1 == t4:
                if mem[-1] != t1:
                    mem.append(t1)
                index2 += 1
            if t2 == t4:
                if mem[-1] != t2:
                    mem.append(t2)
                index3 += 1
            if t3 == t4:
                if mem[-1] != t3:
                    mem.append(t3)
                index5 += 1
        return mem[-1]

# Solution().nthUglyNumber(456)
Solution()._1nthUglyNumber(1690)