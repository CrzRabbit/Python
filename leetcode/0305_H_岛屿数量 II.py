'''
假设你设计一个游戏，用一个 m 行 n 列的 2D 网格来存储你的游戏地图。

起始的时候，每个格子的地形都被默认标记为「水」。我们可以通过使用 addLand 进行操作，将位置 (row, col) 的「水」变成「陆地」。

你将会被给定一个列表，来记录所有需要被操作的位置，然后你需要返回计算出来 每次 addLand 操作后岛屿的数量。

注意：一个岛的定义是被「水」包围的「陆地」，通过水平方向或者垂直方向上相邻的陆地连接而成。你可以假设地图网格的四边均被无边无际的「水」所包围。

请仔细阅读下方示例与解析，更加深入了解岛屿的判定。

示例:

输入: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
输出: [1,1,2,3]
解析:

起初，二维网格 grid 被全部注入「水」。（0 代表「水」，1 代表「陆地」）

0 0 0
0 0 0
0 0 0
操作 #1：addLand(0, 0) 将 grid[0][0] 的水变为陆地。

1 0 0
0 0 0   Number of islands = 1
0 0 0
操作 #2：addLand(0, 1) 将 grid[0][1] 的水变为陆地。

1 1 0
0 0 0   岛屿的数量为 1
0 0 0
操作 #3：addLand(1, 2) 将 grid[1][2] 的水变为陆地。

1 1 0
0 0 1   岛屿的数量为 2
0 0 0
操作 #4：addLand(2, 1) 将 grid[2][1] 的水变为陆地。

1 1 0
0 0 1   岛屿的数量为 3
0 1 0
拓展：

你是否能在 O(k log mn) 的时间复杂度程度内完成每次的计算？（k 表示 positions 的长度）
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    并查集
    '''
    @printTime()
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        n, m = m, n
        mem = set()
        fa = [i for i in range(n * m)]
        rank = [1 for _ in range(n * m)]
        grid = [[0 for _ in range(m)] for _ in range(n)]
        ret = []
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
        for pos in positions:
            x, y = pos[0], pos[1]
            grid[x][y] = 1
            if x > 0 and grid[x - 1][y] == 1:
                if find((x - 1) * m + y) in mem:
                    mem.remove(find((x - 1) * m + y))
                merge((x - 1) * m + y, x * m + y)
            if x < n - 1 and grid[x + 1][y] == 1:
                if find((x + 1) * m + y) in mem:
                    mem.remove(find((x + 1) * m + y))
                merge(x * m + y, (x + 1) * m + y)
            if y > 0 and grid[x][y - 1] == 1:
                if find(x * m + y - 1) in mem:
                    mem.remove(find(x * m + y - 1))
                merge(x * m + y - 1, x * m + y)
            if y < m - 1 and grid[x][y + 1] == 1:
                if find(x * m + y + 1) in mem:
                    mem.remove(find(x * m + y + 1))
                merge(x * m + y, x * m + y + 1)
            mem.add(find(x * m + y))
            ret.append(mem.__len__())
        return ret

m = 4
n = 4
positions = [[0,0], [0,1], [1,2], [2,1], [2,2], [1,1], [2, 3], [3,0],[0,3]]
Solution().numIslands2(m, n, positions)