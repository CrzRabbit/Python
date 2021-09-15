'''
给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

示例 1:

输入: 5
输出: 5
解释:
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
说明: 1 <= n <= 109
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findIntegers(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        mem = []
        t = n
        while t > 0:
            mem.append(1 if t & 1 else 0)
            t >>= 1
        l = len(mem)
        dp = [[0, 0] for _ in range(l)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, l):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]
        def get(l, t, cur):
            cur += t << l
            ans = 0
            if l == 0:
                if t == 0:
                    ans = dp[0][0]
                elif cur <= n:
                    ans = dp[0][1]
            elif t == 0:
                ans = get(l - 1, 1, cur) + get(l - 1, 0, cur)
            else:
                if cur <= n:
                    ans = get(l - 1, 0, cur)
            return ans
        dp[l - 1][1] = get(l - 2, 0, 1 << (l - 1))
        return sum(dp[l - 1])

    @printTime()
    def _1findIntegers(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        mem = []
        t = n
        while t > 0:
            mem.append(1 if t & 1 else 0)
            t >>= 1
        l = len(mem)
        dp = [[0, 0] for _ in range(l)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, l):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]
        return sum(dp[l - 1])

n = 132425
Solution().findIntegers(n)
Solution()._1findIntegers(n)