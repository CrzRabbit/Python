'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。


示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
'''
import queue
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    并查集
    '''
    @printTime()
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fa = [i for i in range(n * m)]
        rank = [1 for _ in range(n * m)]
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
                if grid[i][j] == '0':
                    fa[i * m + j] = -1
                    continue
                if j < m - 1 and grid[i][j] == '1' and grid[i][j + 1] == '1':
                    merge(i * m + j, i * m + j + 1)
                if i < n - 1 and grid[i][j] == '1' and grid[i + 1][j] == '1':
                    merge(i * m + j, (i + 1) * m + j)
        mem = set()
        for i in range(n * m):
            if fa[i] != -1:
                mem.add(find(i))
        return mem.__len__()
    '''
    BFS
    '''
    @printTime()
    def _1numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                cnt += 1
                q = queue.Queue()
                q.put([i, j])
                while not q.empty():
                    x, y = q.get()
                    if x > 0 and grid[x - 1][y] == '1':
                        grid[x - 1][y] = '0'
                        q.put([x - 1, y])
                    if x < n - 1 and grid[x + 1][y] == '1':
                        grid[x + 1][y] = '0'
                        q.put([x + 1, y])
                    if y > 0 and grid[x][y - 1] == '1':
                        grid[x][y - 1] = '0'
                        q.put([x, y - 1])
                    if y < m - 1 and grid[x][y + 1] == '1':
                        grid[x][y + 1] = '0'
                        q.put([x, y + 1])
        return cnt

    '''
    DFS
    '''
    @printTime()
    def _2numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        def dfs(x, y):
            grid[x][y] = '0'
            if x > 0 and grid[x - 1][y] == '1':
                dfs(x - 1, y)
            if x < n - 1 and grid[x + 1][y] == '1':
                dfs(x + 1, y)
            if y > 0 and grid[x][y - 1] == '1':
                dfs(x, y - 1)
            if y < m - 1 and grid[x][y + 1] == '1':
                dfs(x, y + 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                cnt += 1
                dfs(i, j)
        return cnt

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
Solution().numIslands(grid)
Solution()._1numIslands([["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]])
Solution()._2numIslands([['1']])