'''
给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1：
输入：[1, 5, 2]
输出：False
解释：一开始，玩家1可以从1和2中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 False 。

示例 2：
输入：[1, 5, 233, 7]
输出：True
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
     最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。

提示：
1 <= 给定的数组长度 <= 20.
数组里所有分数都为非负数且不会大于 10000000 。
如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。
'''
from typing import List
from leetcode.tools.time import *
from leetcode.tools.tool import *

class Solution:
    '''
    递归 会超时
    '''
    def PredictTheWinner(self, nums: List[int]) -> bool:
        mem = {}
        def pre(nums, player1, dot1, dot2):
            #print(nums, player1, dot1, dot2)
            if len(nums) == 0:
                #print(dot1, dot2)
                return dot1 >= dot2
            elif len(nums) == 1:
                if player1:
                    dot1 += nums[0]
                else:
                    dot2 += nums[0]
                return pre([], not player1, dot1, dot2)
            else:
                if player1:
                    if pre(nums[1:], not player1, dot1 + nums[0], dot2):
                        return pre(nums[1:], not player1, dot1 + nums[0], dot2)
                    if pre(nums[:len(nums) - 1], not player1, dot1 + nums[len(nums) - 1], dot2):
                        return pre(nums[:len(nums) - 1], not player1, dot1 + nums[len(nums) - 1], dot2)
                    return False
                else:
                    if not pre(nums[1:], not player1, dot1, dot2 + nums[0]):
                        return pre(nums[1:], not player1, dot1, dot2 + nums[0])
                    if not pre(nums[:len(nums) - 1], not player1, dot1, dot2 + nums[len(nums) - 1]):
                        return pre(nums[:len(nums) - 1], not player1, dot1, dot2 + nums[len(nums) - 1])
                    return True
        return pre(nums, True, 0, 0)
    '''
    动态规划
    ret[i][j]表示剩余nums[i][j]时，当前玩家能够获取到的与对方玩家的分数最大插值
    1. i > j ret[i][j] = 0
    2. i == j ret[i][j] = nums[i]
    3. i < j ret[i][j] = max(nums[i] - ret[i + 1][j], nums[j] - ret[i][j - 1])
    由于ret[i][j]会使用到ret[i + 1][j]和ret[i][j - 1]，所以i从大到小遍历，j从小到大遍历
    
    如果nums长度为偶数的话，先手的人可以决定自己拿index为奇数的所有分数还是为偶数的所有分数
    ，这两个一定有大小关系，哪个大先手选哪个，所以先手一定赢
    '''
    def _1PredictTheWinner(self, nums: List[int]) -> bool:
        ret = [[0 for i in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)):
            ret[i][i] = nums[i]
        for i in range(len(nums) - 1, - 1, -1):
            for j in range(i + 1, len(nums)):
                ret[i][j] = max(nums[i] - ret[i + 1][j], nums[j] - ret[i][j - 1])
        printMatrix(ret, 10)
        return ret[0][len(nums) - 1] >= 0
nums = [504,427,95,397,468,485,326,112,296,290,106,148,12,334,23,296,122,187,141,187]
#nums = [1, 5, 2]
so = Solution()
printTime()
print(so.PredictTheWinner(nums))
printTime()
print(so._1PredictTheWinner(nums))
printTime()