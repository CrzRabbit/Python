'''
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。



示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。


提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                    continue
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)
        return dp[0][-1]
    '''
    leetcode时间100%解法
    '''
    @printTime()
    def _1longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1 or s == s[::-1]:
            return n
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            prev = 0
            for j in range(i - 1, -1, -1):
                dpj = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                    prev = dpj
                else:
                    if dp[j + 1] > dpj:
                        dp[j] = dp[j + 1]
                    prev = dpj
        return dp[0]

s = "leetcode"
Solution().longestPalindromeSubseq(s)
Solution()._1longestPalindromeSubseq(s)