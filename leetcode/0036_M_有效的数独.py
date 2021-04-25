'''
请你判断一个9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用'.'表示。

注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
'''
class Solution:
    '''
    依次遍历，使用字典数组保存每行，每列，每一片中出现的数字，超过2返回False
    '''
    def isValidSudoku(self, board) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        pieces = [{} for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                t = board[i][j]
                if t != '.':
                    if t not in rows[i]:
                        rows[i][t] = 1
                    else:
                        return False
                    if t not in columns[j]:
                        columns[j][t] = 1
                    else:
                        return False
                    piecesIndex = (i // 3) * 3 + j // 3
                    if t not in pieces[piecesIndex]:
                        pieces[piecesIndex][t] = 1
                    else:
                        return False
        #print(rows, columns, pieces)
        return True
board = \
     [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

so = Solution()
print(so.isValidSudoku(board))