'''
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。



示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

提示：

0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def numDistinct(self, s: str, t: str) -> int:
        lens = len(s)
        lent = len(t)
        dp = [[0 for _ in range(lent + 1)] for _ in range(lens + 1)]
        dp[0][0] = 1
        for i in range(1, lens + 1):
            for j in range(0, lent + 1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] += dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]

# s = "babgbag"
# t = "bag"
s = "rabbbit"
t = "rabbit"
Solution().numDistinct(s, t)