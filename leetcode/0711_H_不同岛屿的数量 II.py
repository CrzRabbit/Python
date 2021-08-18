'''
给定一个非空01二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。

请你计算这个网格中共有多少个形状不同的岛屿。如果两个岛屿的形状相同，或者通过旋转（顺时针旋转 90°，180°，270°）、翻转（左右翻转、上下翻转）后形状相同，那么就认为这两个岛屿是相同的。


样例 1:

11000
10000
00001
00011
给定上图，返回结果 1。

注意 ：

11
1
和

 1
11
是相同的岛屿。因为我们通过 180° 旋转第一个岛屿，两个岛屿的形状相同。

样例 2:

11100
10001
01001
01110
给定上图，返回结果 2。

下面是两个不同的岛屿：
111
1
和
1
1

注意 ：
111
1
和
1
111
相同的岛屿。因为我们通过上下翻转第一个岛屿，两个岛屿的形状相同。

注释 :  二维数组每维的大小都不会超过50。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        pass

grid = [[1,1,0,0,0],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [0,0,0,1,1]]
Solution().numDistinctIslands2(grid)