'''
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。
'''
class Solution:
    def solveSudoku(self, board) -> None:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        pieces = [{} for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                t = board[i][j]
                if t != '.':
                    rows[i][t] = 1
                    columns[j][t] = 1
                    piecesIndex = (i // 3) * 3 + j // 3
                    pieces[piecesIndex][t] = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                t = board[i][j]
                if board == '.':


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
print(so.solveSudoku(board))