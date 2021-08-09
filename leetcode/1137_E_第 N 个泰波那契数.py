'''
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。


示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

示例 2：

输入：n = 25
输出：1389537


提示：

0 <= n <= 37
答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    矩阵快速幂
    '''
    @printTime()
    def tribonacci(self, n: int) -> int:
        base = [[0], [1], [1]]
        if n < 3:
            return base[n][0]
        def pmatrix(a, b):
            ret = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
            for i in range(len(ret)):
                for j in range(len(ret[0])):
                    s = 0
                    for k in range(len(a[0])):
                        s += a[i][k] * b[k][j]
                    ret[i][j] = s
            return ret
        def qpow(k):
            mat = [[0, 1, 0],
                   [0, 0, 1],
                   [1, 1, 1]]
            ans = [[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]
            while k:
                if k & 1:
                    ans = pmatrix(ans, mat)
                mat = pmatrix(mat, mat)
                k >>= 1
            return pmatrix(ans, base)
        return qpow(n - 2)[2][0]

Solution().tribonacci(3)
'''
[0, 1, 0]    Fn       Fn + 1
[0, 0, 1]    Fn + 1   Fn + 2
[1, 1, 1]    Fn + 2   Fn + 3
'''