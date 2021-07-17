'''
有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。

请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。


示例 1：

输入：prob = [0.4], target = 1
输出：0.40000

示例 2：

输入：prob = [0.5,0.5,0.5,0.5,0.5], target = 0
输出：0.03125


提示：

1 <= prob.length <= 1000
0 <= prob[i] <= 1
0 <= target <= prob.length
如果答案与标准答案的误差在 10^-5 内，则被视为正确答案。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    自顶向下
    '''
    @printTime()
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        self.len = len(prob)
        mem = {}
        def dp(n, k):
            if n == 0:
                if k == 0:
                    ans = 1 - prob[0]
                elif k == 1:
                    ans = prob[0]
                else:
                    ans = 0
            else:
                if (n, k) in mem:
                    return mem[(n, k)]
                ans = (1 - prob[n]) * dp(n - 1, k)
                if k > 0:
                    ans += prob[n] * dp(n - 1, k - 1)
            mem[(n, k)] = ans
            return ans
        ret = dp(self.len - 1, target)
        return ret

    '''
    DP
    '''
    @printTime()
    def _1probabilityOfHeads(self, prob: List[float], target: int) -> float:
        self.len = len(prob)
        dp = [[0.0 for _ in range(target + 1)] for _ in range(self.len)]
        dp[0][0] = 1 - prob[0]
        if target > 0:
            dp[0][1] = prob[0]
        for i in range(1, self.len):
            for j in range(target + 1):
                if i < j - 1:
                    continue
                if j == 0:
                    dp[i][j] = (1 - prob[i]) * dp[i - 1][0]
                    continue
                dp[i][j] = (1 - prob[i]) * dp[i - 1][j] + prob[i] * dp[i - 1][j - 1]
        return dp[self.len - 1][target]

prob = [0.5,0.1,0.5,0.5,0.51, 0.1]
Solution().probabilityOfHeads(prob, 3)
Solution()._1probabilityOfHeads(prob, 3)