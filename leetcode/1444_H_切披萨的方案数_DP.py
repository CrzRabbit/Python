'''
给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。

切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，

如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。

请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。


示例 1：

输入：pizza = ["A..","AAA","..."], k = 3
输出：3
解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。

示例 2：

输入：pizza = ["A..","AA.","..."], k = 3
输出：1

示例 3：

输入：pizza = ["A..","A..","..."], k = 1
输出：1

提示：

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza 只包含字符 'A' 和 '.' 。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    递归
    '''
    @printTime()
    def ways(self, pizza: List[str], k: int) -> int:
        self.ret = 0
        self.rows = len(pizza)
        self.cols = len(pizza[0])
        mem = {}
        def re(row, col, n):
            if (row, col, n) in mem:
                return mem[(row, col, n)]
            count = 0
            if n == 1:
                for i in range(row, self.rows):
                    for j in range(col, self.cols):
                        if pizza[i][j] == 'A':
                            count = 1
                mem[(row, col, n)] = count
                return count
            found = False
            for i in range(row, self.rows - 1):
                if not found:
                    for j in range(col, self.cols):
                        if pizza[i][j] == 'A':
                            found = True
                            break
                if found:
                    count += re(i + 1, col, n - 1)
            found = False
            for j in range(col, self.cols - 1):
                if not found:
                    for i in range(row, self.rows):
                        if pizza[i][j] == 'A':
                            found = True
                            break
                if found:
                    count += re(row, j + 1, n - 1)
            mem[(row, col, n)] = count
            return count
        self.ret = re(0, 0, k)
        return self.ret % (10 ** 9 + 7)

    '''
    DP, 未完成
    '''
    @printTime()
    def _1ways(self, pizza: List[str], k: int) -> int:
        self.rows = len(pizza)
        self.cols = len(pizza[0])
        self.frow = [False for _ in range(self.rows)]
        self.fcol = [False for _ in range(self.cols)]
        dp = [[[0 for _ in range(k)] for _ in range(self.cols)] for _ in range(self.rows)]
        if pizza[self.rows - 1][self.cols - 1] == 'A':
            dp[self.rows - 1][self.cols - 1][0] = 1
            self.frow[self.rows - 1] = True
            self.fcol[self.cols - 1] = True
        for j in range(self.cols - 2, -1, -1):
            if dp[self.rows - 1][j + 1][0] or pizza[self.rows - 1][j] == 'A':
                dp[self.rows - 1][j][0] = 1
            found = False
            for a in range(j, self.cols - 1):
                if not found and pizza[self.rows - 1][a] == 'A':
                    self.fcol[a] = True
                    found = True
                if found:
                    for b in range(1, k):
                        dp[self.rows - 1][j][b] += dp[self.rows - 1][a + 1][b - 1]
        for i in range(self.rows - 2, -1, -1):
            if dp[i + 1][self.cols - 1][0] or pizza[i][self.cols - 1] == 'A':
                dp[i][self.cols - 1][0] = 1
            found = False
            for a in range(i, self.rows - 1):
                if not found and pizza[a][self.cols - 1] == 'A':
                    self.frow[a] = True
                    found = True
                if found:
                    for b in range(1, k):
                        dp[i][self.cols - 1][b] += dp[a + 1][self.cols - 1][b - 1]
        for i in range(self.rows - 2, -1, -1):
            for j in range(self.cols - 2, -1, -1):
                if pizza[i][j] == 'A':
                    self.fcol[j] = True
                    self.frow[i] = True
                if pizza[i][j] == 'A' or dp[i + 1][j][0] or dp[i][j + 1][0]:
                    dp[i][j][0] = 1
                found = False
                for a in range(j, self.cols - 1):
                    if not found and self.fcol[a]:
                        found = True
                    if found:
                        for b in range(1, k):
                            dp[i][j][b] += dp[i][a + 1][b - 1]
                found = False
                for a in range(i, self.rows - 1):
                    if not found and self.frow[a]:
                        found = True
                    if found:
                        for b in range(1, k):
                            dp[i][j][b] += dp[a + 1][j][b - 1]
        return dp[0][0][-1] % (10 ** 9 + 7)

pizza = ["..AA..AA..A...",
         "...AA..AAAA...",
         "A..A........AA",
         ".AAAA....AAAA.",
         "A..AAA.A.AAAA.",
         "AAAAAA..AAA.A.",
         "AA.AA..A.A.AA.",
         "AAA...A...AAA.",
         "..AAAAAA..A...",
         "..AA..AA.AAA..",
         ".AAAAA.AAA.A.A",
         "..AAA.....A...",
         "..A.....AA...A",
         ".AAA...A..A.AA",
         "A........A..A."]
k = 3
Solution().ways(pizza, k)
Solution()._1ways(pizza, k)
'''
[[[1, 27, 527], [1, 26, 479], [1, 25, 441], [1, 24, 404], [1, 23, 362], [1, 22, 327], [1, 21, 295], [1, 20, 266], [1, 19, 233], [1, 18, 203], [1, 17, 170], [1, 15, 122], [1, 14, 98], [1, 11, 26]],
 [[1, 26, 489], [1, 25, 443], [1, 24, 407], [1, 23, 372], [1, 22, 332], [1, 21, 299], [1, 20, 269], [1, 19, 242], [1, 18, 211], [1, 17, 183], [1, 16, 152], [1, 14, 107], [1, 13, 85], [1, 11, 26]],
 [[1, 25, 454], [1, 24, 410], [1, 23, 376], [1, 22, 343], [1, 21, 305], [1, 20, 274], [1, 19, 246], [1, 18, 221], [1, 17, 192], [1, 16, 166], [1, 15, 137], [1, 14, 107], [1, 13, 85], [1, 11, 26]], 
 [[1, 24, 410], [1, 23, 368], [1, 22, 336], [1, 21, 305], [1, 20, 269], [1, 19, 240], [1, 18, 214], [1, 17, 191], [1, 16, 164], [1, 15, 140], [1, 14, 113], [1, 13, 85],  [1, 12, 65], [1, 3, 2]], 
 [[1, 23, 375], [1, 22, 335], [1, 21, 305], [1, 20, 276], [1, 19, 242], [1, 18, 215], [1, 17, 191], [1, 16, 170], [1, 15, 145], [1, 14, 123], [1, 13, 98],  [1, 12, 72],  [1, 11, 54], [1, 3, 2]], 
 [[1, 22, 341], [1, 21, 303], [1, 20, 275], [1, 19, 248], [1, 18, 216], [1, 17, 191], [1, 16, 169], [1, 15, 150], [1, 14, 127], [1, 13, 107], [1, 12, 84],  [1, 11, 60],  [1, 10, 44], [1, 3, 2]], 
 [[1, 21, 308], [1, 20, 272], [1, 19, 246], [1, 18, 221], [1, 17, 191], [1, 16, 168], [1, 15, 148], [1, 14, 131], [1, 13, 110], [1, 12, 92],  [1, 11, 71],  [1, 10, 49],  [1, 9, 35],  [1, 3, 2]], 
 [[1, 20, 276], [1, 19, 242], [1, 18, 218], [1, 17, 195], [1, 16, 167], [1, 15, 146], [1, 14, 128], [1, 13, 113], [1, 12, 94],  [1, 11, 78],  [1, 10, 59],  [1, 9, 39],   [1, 8, 27],  [1, 3, 2]], 
 [[1, 19, 243], [1, 18, 211], [1, 17, 189], [1, 16, 168], [1, 15, 142], [1, 14, 123], [1, 13, 107], [1, 12, 94],  [1, 11, 77],  [1, 10, 63],  [1, 9, 46],   [1, 7, 23],   [1, 6, 16],  [1, 3, 2]], 
 [[1, 18, 214], [1, 17, 184], [1, 16, 164], [1, 15, 145], [1, 14, 121], [1, 13, 104], [1, 12, 90],  [1, 11, 79],  [1, 10, 64],  [1, 9, 52],   [1, 8, 37],   [1, 7, 22],   [1, 5, 11],  [1, 3, 2]], 
 [[1, 17, 185], [1, 16, 157], [1, 15, 139], [1, 14, 122], [1, 13, 100], [1, 12, 85],  [1, 10, 65],  [1, 10, 65],  [1, 9, 52],   [1, 8, 42],   [1, 7, 29],   [1, 6, 16],   [1, 5, 11],  [1, 3, 2]], 
 [[1, 16, 150], [1, 15, 124], [1, 14, 108], [1, 13, 93],  [1, 12, 73],  [1, 9, 46],   [1, 9, 46],   [1, 9, 46],   [1, 8, 35],   [1, 7, 27],   [1, 6, 16],   [1, 3, 3],    [1, 3, 3],   [1, 1, 0]], 
 [[1, 15, 122], [1, 14, 98],  [1, 13, 84],  [1, 12, 71],  [1, 8, 35],   [1, 8, 35],   [1, 8, 35],   [1, 8, 35],   [1, 7, 26],   [1, 6, 20],   [1, 5, 11],   [1, 3, 3],    [1, 3, 3],   [1, 1, 0]], 
 [[1, 14, 94],  [1, 13, 72],  [1, 12, 60],  [1, 11, 49],  [1, 7, 21],   [1, 7, 21],   [1, 7, 21],   [1, 7, 21],   [1, 5, 11],   [1, 5, 11],   [1, 4, 4],    [1, 2, 0],    [1, 2, 0],   [1, 0, 0]], 
 [[1, 12, 27],  [1, 3, 0],    [1, 3, 0],    [1, 3, 0],    [1, 3, 0],    [1, 3, 0],    [1, 3, 0],    [1, 3, 0],    [1, 3, 0],    [1, 3, 0],    [1, 0, 0],    [1, 0, 0],    [1, 0, 0],   [0, 0, 0]]]
'''