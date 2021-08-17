'''
可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场
如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

按 总出勤 计，学生缺勤（'A'）严格 少于两天。
学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。
给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 取余 的结果。


示例 1：

输入：n = 2
输出：8
解释：
有 8 种长度为 2 的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。

示例 2：

输入：n = 1
输出：3

示例 3：

输入：n = 10101
输出：183236316

提示：

1 <= n <= 105
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        p = 0 #出现过A并且当前为P
        p0a = 1 #没出现过A且当前为P
        a = 1 #当前为A
        l1 = 0 #出现过A且当前为第一个L
        l10a = 1 #没出现过A且当前为第一个L
        l2 = 0 #出现过A且当前为第二个L
        l20a = 0 #没出现过A且当前为第二个L
        for i in range(1, n):
            tp = (p + a + l1 + l2) % mod
            tp0a = (p0a + l10a + l20a) % mod
            ta = (p0a + l10a + l20a) % mod
            tl1 = (p + a) % mod
            p, a, l1, l2, p0a, l10a, l20a = tp, ta, tl1, l1, tp0a, p0a, l10a
        return (p + p0a + a + l1 + l10a + l2 + l20a) % mod

    '''
    矩阵快速幂
    '''
    @printTime()
    def _1checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def pmatrix(a, b):
            ret = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
            for i in range(len(ret)):
                for j in range(len(ret[0])):
                    s = 0
                    for k in range(len(a[0])):
                        s += a[i][k] * b[k][j]
                    ret[i][j] = s % mod
            return ret

        def qpow3(mat, n, base):
            ans = [[0 for _ in range(len(mat))] for _ in range(len(mat))]
            for i in range(len(mat)):
                ans[i][i] = 1
            while n:
                if n & 1:
                    ans = pmatrix(ans, mat)
                mat = pmatrix(mat, mat)
                n >>= 1
            return pmatrix(base, ans)
        '''
        p = 0 #出现过A并且当前为P
        p0a = 1 #没出现过A且当前为P
        a = 1 #当前为A
        l1 = 0 #出现过A且当前为第一个L
        l10a = 1 #没出现过A且当前为第一个L
        l2 = 0 #出现过A且当前为第二个L
        l20a = 0 #没出现过A且当前为第二个L
        
        tp = (p + a + l1 + l2) % mod
        tp0a = (p0a + l10a + l20a) % mod
        ta = (p0a + l10a + l20a) % mod
        tl1 = (p + a) % mod
        p, a, l1, l2, p0a, l10a, l20a = tp, ta, tl1, l1, tp0a, p0a, l10a
        '''
        base = [[0, 1, 1, 0, 1, 0, 0]]
        mat = [[1, 0, 0, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0],
               [1, 0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0],
               [0, 1, 1, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 0, 0]]
        base = qpow3(mat, n - 1, base)
        ans = sum(pmatrix(base, [[1], [1], [1], [1], [1], [1], [1]])[0])
        return ans

n = 12314
Solution().checkRecord(n)
Solution()._1checkRecord(n)