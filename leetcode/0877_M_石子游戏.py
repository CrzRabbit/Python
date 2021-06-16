'''
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

示例：
输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。

提示：
2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles) 是奇数。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    总数为奇数，所以按照奇数堆，偶数堆分为两个部分，一定有大有小
    先选的可以决定自己能拿到奇数堆部分还是偶数堆部分，所以一定能赢
    '''
    def stoneGame(self, piles: List[int]) -> bool:
        return True

    '''
    DP
    '''
    @printTime()
    def _1stoneGame(self, piles: List[int]) -> bool:
        self.len = len(piles)
        dp = [[0 for j in range(self.len)] for i in range(self.len)]
        for i in range(self.len - 1, - 1, -1):
            for j in range(i, self.len):
                if i == j:
                    dp[i][j] = piles[i]
                else:
                    dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        print(dp)
        return dp[0][self.len - 1] > 0

piles = [5,3,4,5]
Solution()._1stoneGame(piles)