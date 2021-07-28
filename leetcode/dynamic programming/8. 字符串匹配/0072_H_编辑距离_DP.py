'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def minDistance(self, word1: str, word2: str) -> int:
        self.len1 = len(word1)
        self.len2 = len(word2)
        if self.len1 == 0 and self.len2 == 0:
            return 0
        elif self.len1 == 0:
            return self.len2
        elif self.len2 == 0:
            return self.len1
        dp = [[0 for _ in range(self.len2)] for _ in range(self.len1)]
        found1 = False
        found2 = False
        if word1[0] == word2[0]:
            found1 = True
            found2 = True
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for i in range(1, self.len2):
            if word1[0] == word2[i] and not found1:
                found1 = True
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, self.len1):
            if word1[i] == word2[0] and not found2:
                found2 = True
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, self.len1):
            for j in range(1, self.len2):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[-1][-1]

word1 = "horse"
word2 = "ros"
Solution().minDistance(word1, word2)