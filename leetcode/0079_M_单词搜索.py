'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

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
    '''
    双向同时搜索
    '''
    @printTime()
    def exist(self, board: List[List[str]], word: str) -> bool:
        q1 = queue.Queue()
        q2 = queue.Queue()
        n = len(board)
        m = len(board[0])
        cnt = len(word)
        vis = [[[[[], []] for _ in range(cnt + 1)] for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    q1.put([[i, j]])
                    vis[i][j][1][0].append([i, j])
                if board[i][j] == word[-1]:
                    if len(word) == 1:
                        return True
                    q2.put([[i, j]])
                    vis[i][j][cnt][1].append([i, j])
        def found(vis, t):
            for v in vis:
                count = 0
                for tt in t:
                    if tt in v:
                        count += 1
                if count == 1:
                    return True
            return False
        while not q1.empty() and not q2.empty():
            route = q1.get()
            cur = route[-1]
            index = len(route)
            if index == len(word):
                return True
            if cur[0] > 0 and board[cur[0] - 1][cur[1]] == word[index] and [cur[0] - 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] - 1, cur[1]])
                vis[cur[0] - 1][cur[1]][len(t)][0].append(t)
                if found(vis[cur[0] - 1][cur[1]][len(t)][1], t):
                    return True
                q1.put(t)
            if cur[0] < n - 1 and board[cur[0] + 1][cur[1]] == word[index] and [cur[0] + 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] + 1, cur[1]])
                vis[cur[0] + 1][cur[1]][len(t)][0].append(t)
                if found(vis[cur[0] + 1][cur[1]][len(t)][1], t):
                    return True
                q1.put(t)
            if cur[1] > 0 and board[cur[0]][cur[1] - 1] == word[index] and [cur[0], cur[1] - 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] - 1])
                vis[cur[0]][cur[1] - 1][len(t)][0].append(t)
                if found(vis[cur[0]][cur[1] - 1][len(t)][1], t):
                    return True
                q1.put(t)
            if cur[1] < m - 1 and board[cur[0]][cur[1] + 1] == word[index] and [cur[0], cur[1] + 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] + 1])
                vis[cur[0]][cur[1] + 1][len(t)][0].append(t)
                if found(vis[cur[0]][cur[1] + 1][len(t)][1], t):
                    return True
                q1.put(t)

            route = q2.get()
            cur = route[-1]
            index = len(route)
            if index == len(word):
                return True
            if cur[0] > 0 and board[cur[0] - 1][cur[1]] == word[cnt - index - 1] and [cur[0] - 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] - 1, cur[1]])
                vis[cur[0] - 1][cur[1]][cnt + 1 - len(t)][1].append(t)
                if found(vis[cur[0] - 1][cur[1]][cnt + 1 - len(t)][0], t):
                    return True
                q2.put(t)
            if cur[0] < n - 1 and board[cur[0] + 1][cur[1]] == word[cnt - index - 1] and [cur[0] + 1, cur[1]] not in route:
                t = route.copy()
                t.append([cur[0] + 1, cur[1]])
                vis[cur[0] + 1][cur[1]][cnt + 1 - len(t)][1].append(t)
                if found(vis[cur[0] + 1][cur[1]][cnt + 1 - len(t)][0], t):
                    return True
                q2.put(t)
            if cur[1] > 0 and board[cur[0]][cur[1] - 1] == word[cnt - index - 1] and [cur[0], cur[1] - 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] - 1])
                vis[cur[0]][cur[1] - 1][cnt + 1 - len(t)][1].append(t)
                if found(vis[cur[0]][cur[1] - 1][cnt + 1 - len(t)][0], t):
                    return True
                q2.put(t)
            if cur[1] < m - 1 and board[cur[0]][cur[1] + 1] == word[cnt - index - 1] and [cur[0], cur[1] + 1] not in route:
                t = route.copy()
                t.append([cur[0], cur[1] + 1])
                vis[cur[0]][cur[1] + 1][cnt + 1 - len(t)][1].append(t)
                if found(vis[cur[0]][cur[1] + 1][cnt + 1 - len(t)][0], t):
                    return True
                q2.put(t)
        return False

board = [["A","A","A","A","A","A"],
         ["A","A","A","A","A","A"],
         ["A","A","A","A","A","A"],
         ["A","A","A","A","A","A"],
         ["A","A","A","A","A","A"],
         ["A","A","A","B","A","A"]]
word = "AAAAAAAABAAAAAB"
Solution().exist(board, word)