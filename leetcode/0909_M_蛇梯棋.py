'''
N x N 的棋盘 board 上，按从 1 到 N*N 的数字给方格编号，编号 从左下角开始，每一行交替方向。

例如，一块 6 x 6 大小的棋盘，编号如下：


r 行 c 列的棋盘，按前述方法编号，棋盘格中可能存在 “蛇” 或 “梯子”；如果 board[r][c] != -1，那个蛇或梯子的目的地将会是 board[r][c]。

玩家从棋盘上的方格 1 （总是在最后一行、第一列）开始出发。

每一回合，玩家需要从当前方格 x 开始出发，按下述要求前进：

选定目标方格：从编号为 x+1，x+2，x+3，x+4，x+5，或者 x+6 的方格中选出一个作为目标方格 s ，目标方格的编号 <= N*N。
该选择模拟了掷骰子的情景，无论棋盘大小如何，你的目的地范围也只能处于区间 [x+1, x+6] 之间。
传送玩家：如果目标方格 S 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 S 。
注意，玩家在每回合的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，你也不会继续移动。

返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 -1。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    BFS
    '''
    @printTime()
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        N2 = N * N
        step = 0
        visit = [False for _ in range(N2)]
        cur = set()
        cur.add(0)
        def getValue(index):
            row = N - 1 - (index // N)
            if (index // N) % 2 == 0:
                column = index % N
            else:
                column = N - 1 - (index % N)
            return board[row][column]
        while len(cur):
            if cur.__contains__(N2 - 1):
                return step
            temp = set()
            for c in cur:
                visit[c] = True
            for c in cur:
                for x in range(1, 7):
                    if c + x >= N2:
                        break
                    value = getValue(c + x)
                    if value != -1:
                        if not visit[value - 1]:
                            temp.add(value - 1)
                    else:
                        if not visit[c + x]:
                            temp.add(c + x)
            cur = temp
            step += 1
        return -1
board = [[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]]
Solution().snakesAndLadders(board)