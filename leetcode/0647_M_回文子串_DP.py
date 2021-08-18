'''

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。


示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

提示：

输入的字符串长度不会超过 1000 。
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                    count += 1
                    continue
                if s[i] == s[j] and (dp[i + 1][j - 1] or i + 1 == j):
                    dp[i][j] = True
                    count += 1
        return count

Solution().countSubstrings("aba" * 1000)