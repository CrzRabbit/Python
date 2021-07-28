'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

提示：
1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
'''
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        table = []
        temp = [0 for i in range(n)]
        ret = []
        def isValid(i, j):
            for t in table:
                if t[0] == i or t[1] == j or (t[0] - i)/(t[1] - j) == -1.0 or (t[0] - i)/(t[1] - j) == 1.0:
                    return False
            return True
        i = 0
        while i < n and i >= 0:
            j = temp[i]
            while j < n:
                if isValid(i, j):
                    table.append([i, j])
                    if i == n - 1:
                        #print(table)
                        r = []
                        for t in table:
                            r.append('.' * (t[1]) + 'Q' + '.' * (n - t[1] - 1))
                        ret.append(r)
                        table = table[:-1]
                    temp[i] = j + 1
                    break
                j += 1
            if j == n or i == n - 1:
                temp[i] = 0
                i -= 1
                table = table[:-1]
                continue
            i += 1
        return ret

so = Solution()
print(so.solveNQueens(4))