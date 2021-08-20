'''
给定一个包含了一些 0 和 1 的非空二维数组  grid 。

一个  岛屿  是由一些相邻的  1  (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设  grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)


示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回  6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回  0。

注意:  给定的矩阵grid  的长度和宽度都不超过 50。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fa = [i for i in range(n * m)]
        rank = [1 for _ in range(n * m)]
        mem = {}
        def find(idx):
            if idx == fa[idx]:
                return fa[idx]
            fa[idx] = find(fa[idx])
            return fa[idx]
        def merge(idx1, idx2):
            fa1 = find(idx1)
            fa2 = find(idx2)
            if rank[fa1] >= rank[fa2]:
                fa[fa2] = fa1
            else:
                fa[fa1] = fa2
            if rank[fa1] == rank[fa2] and fa1 != fa2:
                rank[fa1] += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i > 0 and grid[i - 1][j] == 1:
                        merge((i - 1) * m + j, i * m + j)
                    if j > 0 and grid[i][j - 1] == 1:
                        merge(i * m + j - 1, i * m + j)
        ret = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    f = find(i * m + j)
                    if f not in mem:
                        mem[f] = 1
                    else:
                        mem[f] += 1
                    ret = max(ret, mem[f])
        return ret

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
Solution().maxAreaOfIsland(grid)