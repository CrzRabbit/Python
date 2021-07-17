'''
给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

示例 1:

输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

示例 2:

输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。

注意:

0 < s1.length, s2.length <= 1000。
所有字符串中的字符ASCII值在[97, 122]之间。
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.len1 = len(s1)
        self.len2 = len(s2)
        dp = [[0 for _ in range(self.len2)] for _ in range(self.len1)]
        found1 = False
        found2 = False
        if s1[0] == s2[0]:
            dp[0][0] = 0
            found1 = True
            found2 = True
        else:
            dp[0][0] = ord(s1[0]) + ord(s2[0])
        for i in range(1, self.len2):
            if s1[0] == s2[i] and not found1:
                found1 = True
                dp[0][i] = dp[0][i - 1] - ord(s2[i])
            else:
                dp[0][i] = dp[0][i - 1] + ord(s2[i])
        for i in range(1, self.len1):
            if s1[i] == s2[0] and not found2:
                found2 = True
                dp[i][0] = dp[i - 1][0] - ord(s1[i])
            else:
                dp[i][0] += dp[i - 1][0] + ord(s1[i])
        for i in range(1, self.len1):
            for j in range(1, self.len2):
                dp[i][j] = min(dp[i][j - 1] + ord(s2[j]), dp[i - 1][j] + ord(s1[i]))
                if s1[i] == s2[j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        return dp[-1][-1]

s1 = "sea"
s2 = "eat"
Solution().minimumDeleteSum(s1, s2)
Solution()._1minimumDeleteSum(s1, s2)