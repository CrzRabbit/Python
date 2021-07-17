'''
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。

说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        self.len = len(primes)
        mem = [1]
        index = [0 for _ in range(self.len)]
        while mem.__len__() < n:
            temp = [mem[index[i]] * primes[i] for i in range(self.len)]
            t = min(temp)
            if t != mem[-1]:
                mem.append(t)
            for i in range(self.len):
                if temp[i] == t:
                    index[i] += 1
        return mem[-1]
n = 12
primes = [2, 7, 13, 19]
Solution().nthSuperUglyNumber(n, primes)