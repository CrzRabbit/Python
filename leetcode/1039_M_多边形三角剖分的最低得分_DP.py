'''
给定 N，想象一个凸 N 边多边形，其顶点按顺时针顺序依次标记为 A[0], A[i], ..., A[N-1]。

假设您将多边形剖分为 N-2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 N-2 个三角形的值之和。

返回多边形进行三角剖分后可以得到的最低分。


示例 1：

输入：[1,2,3]
输出：6
解释：多边形已经三角化，唯一三角形的分数为 6。

示例 2：

输入：[3,7,4,5]
输出：144
解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。

示例 3：

输入：[1,3,1,4,1,5]
输出：13
解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。


提示：

3 <= A.length <= 50
1 <= A[i] <= 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    记忆化搜索
    '''
    @printTime()
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        mem = {}
        def recursion(left, right):
            if (left, right) in mem:
                return mem[(left, right)]
            ans = 0
            if left + 2 > right:
                ans = 0
            elif left + 2 == right:
                ans = values[left] * values[left + 1] * values[right]
            else:
                ans = values[left] * values[left + 1] * values[right] + recursion(left + 1, right)
                for i in range(left + 2, right):
                    ans = min(ans, values[left] * values[i] * values[right] + recursion(left, i) + recursion(i, right))
            mem[(left, right)] = ans
            return ans
        recursion(0, n - 1)
        return mem[(0, n - 1)]
    '''
    DP
    '''
    @printTime()
    def _1minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if j == i + 2:
                    dp[i][j] = values[i] * values[i + 1] * values[i + 2]
                    continue
                dp[i][j] = values[i] * values[i + 1] * values[j] + dp[i + 1][j]
                for k in range(i + 2, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + values[i] * values[k] * values[j] + dp[k][j])
        return dp[0][-1]

values = [1,3,1,4,1,5]
Solution().minScoreTriangulation(values)
Solution()._1minScoreTriangulation(values)