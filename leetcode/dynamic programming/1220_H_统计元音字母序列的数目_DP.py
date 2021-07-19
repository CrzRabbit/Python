'''

给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音 'a' 后面都只能跟着 'e'
每个元音 'e' 后面只能跟着 'a' 或者是 'i'
每个元音 'i' 后面 不能 再跟着另一个 'i'
每个元音 'o' 后面只能跟着 'i' 或者是 'u'
每个元音 'u' 后面只能跟着 'a'
由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。



示例 1：

输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
示例 2：

输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
示例 3：

输入：n = 5
输出：68

提示：

1 <= n <= 2 * 10^4
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(2)]
        dp[0] = [1, 1, 1, 1, 1]
        MAGIC = 10 ** 9 + 7
        for i in range(1, n):
            dp[1][0] = (dp[0][1] + dp[0][2] + dp[0][4]) % MAGIC
            dp[1][1] = (dp[0][0] + dp[0][2]) % MAGIC
            dp[1][2] = (dp[0][1] + dp[0][3]) % MAGIC
            dp[1][3] = dp[0][2] % MAGIC
            dp[1][4] = (dp[0][2] + dp[0][3]) % MAGIC
            dp[0] = dp[1]
            dp[1] = [0, 0, 0, 0, 0]
        return sum(dp[0]) % MAGIC

    '''
    使用矩阵快速幂计算
    '''
    @printTime()
    def _1countVowelPermutation(self, n: int) -> int:
        

Solution().countVowelPermutation(200000)
Solution()._1countVowelPermutation(200000)