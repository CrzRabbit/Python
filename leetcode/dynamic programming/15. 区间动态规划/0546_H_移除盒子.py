'''
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。

你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k * k 个积分。

当你将所有盒子都去掉之后，求你能获得的最大积分和。



示例 1：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
----> [1, 3, 3, 3, 1] (1*1=1 分)
----> [1, 1] (3*3=9 分)
----> [] (2*2=4 分)

示例 2：

输入：boxes = [1,1,1]
输出：9

示例 3：

输入：boxes = [1]
输出：1


提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        def getValue(i, j, t):
            ret = 0
            count = 0
            left = None
            for k in range(i, j + 1):
                if boxes[k] == t:
                    count += 1
                    if left is not None:
                        ret += dp[left][k - 1]
                        left = None
                elif left is None:
                    left = k
            if left is not None:
                ret += dp[left][j]
            ret += count ** 2
            return ret
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                temp = set()

        print(dp)
        return dp[0][-1]

boxes = [6,10,1,7,1,3,10,2,1,3]
Solution().removeBoxes(boxes)