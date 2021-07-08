'''
大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 任意 两道餐品做一顿大餐。

给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i​​​​​​​​​​​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 109 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。



示例 1：

输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

示例 2：

输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
 

提示：

1 <= deliciousness.length <= 105
0 <= deliciousness[i] <= 220
'''
from typing import List, Counter

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def countPairs(self, deliciousness: List[int]) -> int:
        mem1 = dict(Counter(deliciousness))
        ret = 0
        mem2 = [2 ** i for i in range(22)]
        for j in mem1:
            for i in mem2:
                t = i - j
                if t in mem1:
                    ret += mem1[j] * mem1[t] if t != j else mem1[j] * (mem1[j] - 1) // 2
            mem1[j] = 0
        return ret % (10 ** 9 + 7)

deliciousness = [149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]
Solution().countPairs(deliciousness)