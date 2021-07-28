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
        # pizza = self.pizza
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
    DP
    '''
    @printTime()
    def _1ways(self, pizza: List[str], k: int) -> int:
        # pizza = self.pizza
        self.rows = len(pizza)
        self.cols = len(pizza[0])
        self.fcol = [False for _ in range(self.cols)]
        dp = [[[0 for _ in range(k)] for _ in range(self.cols)] for _ in range(self.rows)]
        if pizza[self.rows - 1][self.cols - 1] == 'A':
            dp[self.rows - 1][self.cols - 1][0] = 1
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
                    found = True
                if found:
                    for b in range(1, k):
                        dp[i][self.cols - 1][b] += dp[a + 1][self.cols - 1][b - 1]
        for i in range(self.rows - 2, -1, -1):
            for j in range(self.cols - 2, -1, -1):
                if pizza[i][j] == 'A':
                    self.fcol[j] = True
                if pizza[i][j] == 'A' or dp[i + 1][j][0] or dp[i][j + 1][0]:
                    dp[i][j][0] = 1
                found = False
                for a in range(i, self.rows - 1):
                    if not found:
                        for l in range(j, self.cols):
                            if pizza[a][l] == 'A':
                                found = True
                                break
                    if found:
                        for b in range(1, k):
                            dp[i][j][b] += dp[a + 1][j][b - 1]
                found = False
                for a in range(j, self.cols - 1):
                    if not found and self.fcol[a]:
                        found = True
                    if found:
                        for b in range(1, k):
                            dp[i][j][b] += dp[i][a + 1][b - 1]
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
k=4
Solution().ways(pizza, k)
Solution()._1ways(pizza, k)