'''
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。


示例 1：

输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O'
相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

示例 2：

输入：board = [["X"]]
输出：[["X"]]

提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        fa = [i for i in range(m * n)]
        rank = [1 for i in range(m * n)]

        def find(idx):
            if idx != fa[idx]:
                fa[idx] = find(fa[idx])
            return fa[idx]

        def merge(idx1, idx2):
            fa1 = find(idx1)
            fa2 = find(idx2)
            # if rank[fa1] >= rank[fa2]:
            #     fa[fa2] = fa1
            # else:
            #     fa[fa1] = fa2
            # if rank[fa1] == rank[fa2] and fa1 != fa2:
            #     rank[fa1] += 1
            if fa1 == 0:
                fa[fa2] = fa1
            else:
                fa[fa1] = fa2
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if i > 0 and board[i - 1][j] == 'O':
                        merge((i - 1) * m + j, i * m + j)
                    if j > 0 and board[i][j - 1] == 'O':
                        merge(i * m + j - 1, i * m + j)
                if board[i][j] == 'X' or i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    merge(0, i * m + j)
        for i in range(n):
            for j in range(m):
                if find(i * m + j) != 0:
                    board[i][j] = 'X'

board = [["X","X","X","X","O","X"],
         ["O","X","X","O","O","X"],
         ["X","O","X","O","O","O"],
         ["X","O","O","O","X","O"],
         ["O","O","X","X","O","X"],
         ["X","O","X","O","X","X"]]
Solution().solve(board)