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
import bisect
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        mem = [[0 for _ in range(101)] for _ in range(n + 1)]
        for i, box in enumerate(boxes):
            mem[i + 1] = mem[i].copy()
            mem[i + 1][box] += 1
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
            ret += count ** 2
            return ret
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                temp = []
                for k in range(101):
                    if mem[j + 1][k] - mem[i][k] > 0:
                        bisect.insort(temp, [mem[j + 1][k] - mem[i][k], k])
                t1 = []
                for k in range(len(temp)):
                    t1.append(getValue(i, j, temp[k][1]))
                dp[i][j] = max(t1)
        return dp[0][-1]
    @printTime()
    def _1removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        temp = []
        t = boxes[0]
        count = 1
        for i in range(1, n):
            if boxes[i] != t:
                temp.append([t, count])
                t = boxes[i]
                count = 1
            else:
                count += 1
        boxes = temp
        def getValue(i, j, t):
            ret = 0
            count = 0
            left = None
            for k in range(i, j + 1):
                if boxes[k][0] == t:
                    count += boxes[k][1]
                    if left is not None:
                        ret += dp[left][k - 1]
                        left = None
                elif left is None:
                    left = k
            ret += count ** 2
            return ret
        def getIndexs(indexs):
            ret = []
            for i in range(len(indexs)):
                temp = [_ for _ in range(i + 1)]
                while temp[0] <= len(indexs) - i - 1:
                    ret.append(temp.copy())
                    temp[-1] += 1
                    if temp[-1] >= len(indexs) and len(temp) > 1:
                        for j in range(len(temp) - 2, -1, -1):
                            if temp[j] < len(indexs) - (len(temp) - 1 - j):
                                temp[j] += 1
                                temp[j + 1] = temp[j] + 1
            return ret
        n = len(boxes)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = boxes[i][1] ** 2
                    continue
                t1 = []
                for k in range(i, j + 1):
                    if boxes[k][0] == boxes[i][0]:
                        t1.append(k)
                indexs1 = getIndexs(t1)
                print(t1, indexs1)
                for index in indexs1:
                    temp = 0
                    count = 0
                    if t1[index[0]] > i:
                        temp += dp[i][t1[index[0]] - 1]
                    if t1[index[-1]] < j:
                        temp += dp[t1[index[-1]] + 1][j]
                    for k in range(len(index)):
                        count += boxes[t1[index[k]]][1]
                        if k < len(index) - 1:
                            temp += dp[t1[index[k]] + 1][t1[index[k + 1]] - 1]
                    dp[i][j] = max(dp[i][j], temp + count ** 2)
                t2 = []
                for k in range(i, j + 1):
                    if boxes[k][0] == boxes[j][0]:
                        t2.append(k)
                indexs2 = getIndexs(t2)
                print(t2, indexs2)
                for index in indexs2:
                    temp = 0
                    count = 0
                    if t2[index[0]] > i:
                        temp += dp[i][t2[index[0]] - 1]
                    if t2[index[-1]] < j:
                        temp += dp[t2[index[-1]] + 1][j]
                    for k in range(len(index)):
                        count += boxes[t2[index[k]]][1]
                        if k < len(index) - 1:
                            temp += dp[t2[index[k]] + 1][t2[index[k + 1]] - 1]
                    dp[i][j] = max(dp[i][j], temp + count ** 2)
        print(dp)
        return dp[0][-1]

boxes = [6,10,1,7,1,3,10,2,1,3]
Solution().removeBoxes(boxes)
Solution()._1removeBoxes(boxes)