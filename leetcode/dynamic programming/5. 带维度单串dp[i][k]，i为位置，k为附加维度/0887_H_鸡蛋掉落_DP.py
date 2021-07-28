'''
给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

示例 1：
输入：k = 1, n = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
如果它没碎，那么肯定能得出 f = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。

示例 2：
输入：k = 2, n = 6
输出：3

示例 3：
输入：k = 3, n = 14
输出：4

提示：
1 <= k <= 100
1 <= n <= 104
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0 for _ in range(k)] for _ in range(n + 1)]
        for i in range(k):
            dp[1][i] = 1
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(2, n + 1):
            for j in range(1, k):
                left = 1
                right = i
                while left < right:
                    mid = (left + right) >> 1
                    if dp[mid][j - 1] == dp[i - mid][j]:
                        left = mid
                        break
                    elif dp[mid][j - 1] < dp[i - mid][j]:
                        left = mid + 1
                    else:
                        right = mid
                dp[i][j] = max(dp[left - 1][j - 1], dp[i - left][j]) + 1
        return dp[n][k - 1]
    '''
    自顶向下
    '''
    @printTime()
    def _2superEggDrop(self, k: int, n: int) -> int:
        mem = {}
        def dp(k, n):
            if (k, n) in mem:
                return mem[(k, n)]
            if n <= 1:
                ans = 1
            elif k == 1:
                ans = n
            else:
                left = 0
                right = n
                while left < right:
                    mid = (left + right) >> 1
                    t1 = dp(k - 1, mid - 1)
                    t2 = dp(k, n - mid)
                    if t1 == t2:
                        left = mid
                        break
                    elif t1 < t2:
                        left = mid + 1
                    else:
                        right = mid
                ans = max(dp(k - 1, left - 1), dp(k, n - left)) + 1
            mem[k, n] = ans
            return ans
        return dp(k, n)
    '''
    官方题解，自顶向下
    '''
    @printTime()
    def _1superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 x values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(k, n)

#Solution().superEggDrop(100, 8192)
Solution()._1superEggDrop(55, 8000)
Solution()._2superEggDrop(55, 8000)
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14