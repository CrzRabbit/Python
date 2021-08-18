'''
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。


示例 1：

输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]

示例 2：

输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]

提示：

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] 是一个小写英文字母
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] 由小写英文字母组成
words 中的所有字符串互不相同
'''
import queue
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def exist(board: List[List[str]], word: str) -> bool:
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
                if cur[0] > 0 and board[cur[0] - 1][cur[1]] == word[cnt - index - 1] and [cur[0] - 1,
                                                                                          cur[1]] not in route:
                    t = route.copy()
                    t.append([cur[0] - 1, cur[1]])
                    vis[cur[0] - 1][cur[1]][cnt + 1 - len(t)][1].append(t)
                    if found(vis[cur[0] - 1][cur[1]][cnt + 1 - len(t)][0], t):
                        return True
                    q2.put(t)
                if cur[0] < n - 1 and board[cur[0] + 1][cur[1]] == word[cnt - index - 1] and [cur[0] + 1,
                                                                                              cur[1]] not in route:
                    t = route.copy()
                    t.append([cur[0] + 1, cur[1]])
                    vis[cur[0] + 1][cur[1]][cnt + 1 - len(t)][1].append(t)
                    if found(vis[cur[0] + 1][cur[1]][cnt + 1 - len(t)][0], t):
                        return True
                    q2.put(t)
                if cur[1] > 0 and board[cur[0]][cur[1] - 1] == word[cnt - index - 1] and [cur[0],
                                                                                          cur[1] - 1] not in route:
                    t = route.copy()
                    t.append([cur[0], cur[1] - 1])
                    vis[cur[0]][cur[1] - 1][cnt + 1 - len(t)][1].append(t)
                    if found(vis[cur[0]][cur[1] - 1][cnt + 1 - len(t)][0], t):
                        return True
                    q2.put(t)
                if cur[1] < m - 1 and board[cur[0]][cur[1] + 1] == word[cnt - index - 1] and [cur[0],
                                                                                              cur[1] + 1] not in route:
                    t = route.copy()
                    t.append([cur[0], cur[1] + 1])
                    vis[cur[0]][cur[1] + 1][cnt + 1 - len(t)][1].append(t)
                    if found(vis[cur[0]][cur[1] + 1][cnt + 1 - len(t)][0], t):
                        return True
                    q2.put(t)
            return False
        ret = []
        for word in words:
            if exist(board, word):
                ret.append(word)
        return ret

board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
Solution().findWords(board, words)