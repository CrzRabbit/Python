'''
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。
'''
class Solution:
    def shwoSudoku(self, board):
        for i in range(len(board)):
            ret = ''
            for j in range(len(board[0])):
                ret += "{0:^3s}".format(board[i][j])
            print(ret)
        print("   ")

    def solveSudoku(self, board) -> None:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        pieces = [{} for i in range(9)]
        table = [[1 for i in range(9)] for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                t = board[i][j]
                if t != '.':
                    rows[i][t] = 1
                    columns[j][t] = 1
                    piecesIndex = (i // 3) * 3 + j // 3
                    pieces[piecesIndex][t] = 1
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                t = board[i][j]
                k = table[i][j]
                print(i, j, t, k)
                self.shwoSudoku(board)
                piecesIndex = (i // 3) * 3 + j // 3
                if t == '.' or int(t) < k:
                    while k < 10:
                        ks = '{}'.format(k)
                        if (ks not in rows[i] or rows[i][ks] == 0) and (ks not in columns[j] or columns[j][ks] == 0) and (ks not in pieces[piecesIndex] or pieces[piecesIndex][ks] == 0):
                            if t in rows[i]:
                                rows[i][t] = 0
                            if t in columns[j]:
                                columns[j][t] = 0
                            if t in pieces[piecesIndex]:
                                pieces[piecesIndex][t] = 0
                            board[i][j] = ks
                            table[i][j] = k + 1
                            rows[i][ks] = 1
                            columns[j][ks] = 1
                            pieces[piecesIndex][ks] = 1
                            break
                        k += 1
                    t = board[i][j]
                    piecesIndex = (i // 3) * 3 + j // 3
                    print(i, j, t, k)
                    self.shwoSudoku(board)
                    if k == 10:
                        while i >= 0 and (k == 10 or int(t) >= k):
                            if k == 10:
                                if t in rows[i]:
                                    rows[i][t] = 0
                                if t in columns[j]:
                                    columns[j][t] = 0
                                if t in pieces[piecesIndex]:
                                    pieces[piecesIndex][t] = 0
                                board[i][j] = '.'
                                table[i][j] = 1
                            if j > 0:
                                j -= 1
                            else:
                                i -= 1
                                j = 8
                            t = board[i][j]
                            k = table[i][j]
                            piecesIndex = (i // 3) * 3 + j // 3
                        continue
                j += 1
            i += 1
        self.shwoSudoku(board)

board = \
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
so = Solution()
so.solveSudoku(board)