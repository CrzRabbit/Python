'''
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。


示例 1：

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
示例 2：

输入：points = [[1,1],[2,2],[3,3]]
输出：2
示例 3：

输入：points = [[1,1]]
输出：0

提示：

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
所有点都 互不相同
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        for i in range(n):
            mem = {}
            for j in range(n):
                if i == j:
                    continue
                t = ((points[j][0] - points[i][0]) ** 2) + ((points[j][1] - points[i][1]) ** 2)
                if t not in mem:
                    mem[t] = 1
                else:
                    ans += mem[t] << 1
                    mem[t] += 1
        return ans

points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
Solution().numberOfBoomerangs(points)