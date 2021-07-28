'''
给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：

你挑选 任意 一块披萨。
Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
重复上述过程直到没有披萨剩下。
每一块披萨的大小按顺时针方向由循环数组 slices 表示。

请你返回你可以获得的披萨大小总和的最大值。



示例 1：

输入：slices = [1,2,3,4,5,6]
输出：10
解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。

示例 2：

输入：slices = [8,9,8,6,1,1]
输出：16
解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。

示例 3：

输入：slices = [4,1,2,5,8,3,1,9,7]
输出：21

示例 4：

输入：slices = [3,1,2]
输出：3


提示：

1 <= slices.length <= 500
slices.length % 3 == 0
1 <= slices[i] <= 1000
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    可以看作3n块披萨中在不能取相邻两块的情况下取n块取到最多披萨
    '''
    @printTime()
    def maxSizeSlices(self, slices: List[int]) -> int:
        self.len = len(slices)
        if self.len == 3:
            return max(slices)
        ret = 0
        n = self.len // 3
        '''
        dp[i][j]: 
        0 <= j < n的时候表示取到第i块披萨在能取第0块的情况下总共取j + 1块的最大值
        n <= j < 2n的时候表示取到第i块披萨在不能取第0块的情况下总共取j + 1 - n块的最大值
        因为在取到最后一块披萨的时候不能取第0块，需要用到n <= j < 2n部分的数据
        '''
        dp = [[0 for _ in range(n << 1)] for _ in range(3)]
        dp[0][0] = slices[0]
        dp[1][0] = max(slices[1], slices[0])
        dp[1][n] = slices[1]
        for i in range(2, self.len):
            dp[2][0] = max(slices[i], dp[1][0])
            dp[2][n] = max(slices[i], dp[1][n])
            for j in range(1, n):
                dp[2][j] = max(dp[1][j], slices[i] + dp[0][j - 1])
                dp[2][n + j] = max(dp[1][n + j], slices[i] + dp[0][n + j - 1])
            if i == self.len - 1:
                ret = max(ret, dp[2][(n << 1) - 1])
            else:
                ret = max(ret, dp[2][n - 1])
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = [0] * (n << 1)
        return ret

slices = [3,7,8,6,3,10,4,2,9] * 300
Solution().maxSizeSlices(slices)