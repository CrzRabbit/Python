'''
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

示例 1：
输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

示例 2：
输入：stones = [31,26,33,21,40]
输出：5

示例 3：
输入：stones = [1,2]
输出：1

提示：
1 <= stones.length <= 30
1 <= stones[i] <= 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def lastsw(stones):
            l = len(stones)
            if l == 0:
                return 0
            elif l == 1:
                return stones[0]
            elif l == 2:
                return abs(stones[1] - stones[0])
            ret = float('inf')
            for i in range(l - 1):
                for j in range(i + 1, l):
                    t1 = stones[:i] + stones[i + 1:j] + stones[j + 1:]
                    t1.append(abs(stones[i] - stones[j]))
                    temp = lastsw(t1)
                    if ret > temp:
                        ret = temp
            return ret
        return lastsw(stones)

    @printTime()
    def _1lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        hl = s // 2 + 1
        ret = [0 for i in range(hl)]
        for x in stones:
            for i in range(hl - 1, x - 1, - 1):
                ret[i] = max(ret[i], ret[i - x] + x)
        return s - 2 * ret[hl - 1]

stones = []
so = Solution()
so.lastStoneWeightII(stones)
so._1lastStoneWeightII(stones)