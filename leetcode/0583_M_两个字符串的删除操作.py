'''
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例：
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

提示：
给定单词的长度不超过500。
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def minDistance(self, word1: str, word2: str) -> int:
        self.len1 = len(word1)
        self.len2 = len(word2)
        dp = [[0 for _ in range(self.len2)] for _ in range(self.len1)]
        found = False
        for j in range(self.len2):
            if not found and word1[0] == word2[j]:
                found = True
            if found:
                dp[0][j] = j
            else:
                dp[0][j] = j + 2
        found = False
        for i in range(self.len1):
            if not found and word2[0] == word1[i]:
                found = True
            if found:
                dp[i][0] = i
            else:
                dp[i][0] = i + 2
        for i in range(1, self.len1):
            for j in range(1, self.len2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[self.len1 - 1][self.len2 - 1]

w1 = "seaa"
w2 = "eata"
Solution().minDistance(w1, w2)