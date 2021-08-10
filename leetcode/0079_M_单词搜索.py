'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成

进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
'''
import queue
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def exist(self, board: List[List[str]], word: str) -> bool:
        q = queue.Queue()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    q.put([[i, j]])
        while not q.empty():
            route = q.get()
            cur = route[-1]
            index = len(route)
            if index == len(word):
                return True
            if cur[0] > 0 and board[cur[0] - 1][cur[1]] == word[index] and [cur[0] - 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] - 1, cur[1]])
                q.put(t)
            if cur[0] < n - 1 and board[cur[0] + 1][cur[1]] == word[index] and [cur[0] + 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] + 1, cur[1]])
                q.put(t)
            if cur[1] > 0 and board[cur[0]][cur[1] - 1] == word[index] and [cur[0], cur[1] - 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] - 1])
                q.put(t)
            if cur[1] < m - 1 and board[cur[0]][cur[1] + 1] == word[index] and [cur[0], cur[1] + 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] + 1])
                q.put(t)
        return False

    @printTime()
    def _1exist(self, board: List[List[str]], word: str) -> bool:
        q = queue.Queue()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    q.put([[i, j]])
        while not q.empty():
            route = q.get()
            cur = route[-1]
            index = len(route)
            if index == len(word):
                return True
            if cur[0] > 0 and board[cur[0] - 1][cur[1]] == word[index] and [cur[0] - 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] - 1, cur[1]])
                q.put(t)
            if cur[0] < n - 1 and board[cur[0] + 1][cur[1]] == word[index] and [cur[0] + 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] + 1, cur[1]])
                q.put(t)
            if cur[1] > 0 and board[cur[0]][cur[1] - 1] == word[index] and [cur[0], cur[1] - 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] - 1])
                q.put(t)
            if cur[1] < m - 1 and board[cur[0]][cur[1] + 1] == word[index] and [cur[0], cur[1] + 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] + 1])
                q.put(t)
        return False


# board = [["A","B","C","E"],
#          ["S","F","E","S"],
#          ["A","D","E","E"]]
# word = "ABCESEEEFS"
# Solution().exist(board, word)
board1 = [["A","A","A","A","A","A"],
          ["A","A","A","A","A","A"],
          ["A","A","A","A","A","A"],
          ["A","A","A","A","A","A"],
          ["A","A","A","A","A","A"],
          ["A","A","A","A","A","A"]]
word1 = "AAAAAAAAAAAAAAA"
Solution()._1exist(board1, word1)