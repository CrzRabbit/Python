'''
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。


示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。


提示：

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
'''
import queue
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    BFS
    '''
    @printTime()
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        ret = 0
        wordList = [beginWord] + wordList + [endWord]
        n = len(wordList)
        mem = {}
        def same(str1, str2):
            if len(str1) != len(str2):
                return False
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
                if count > 1:
                    return False
            return True
        for i in range(n - 1):
            for j in range(i + 1, n):
                if same(wordList[i], wordList[j]):
                    if i not in mem:
                        mem[i] = []
                    if j not in mem:
                        mem[j] = []
                    mem[i].append(j)
                    mem[j].append(i)
        q = queue.Queue()
        visited = [False for i in range(n)]
        q.put([0, [0]])
        while not q.empty():
            index, route = q.get()
            if wordList[index] == endWord:
                if ret == 0 or len(route) < ret:
                    ret = len(route)
                else:
                    break
            for i in mem[index]:
                if i not in route and visited[i] == False:
                    t = route.copy()
                    t.append(i)
                    q.put([i, t])
                    visited[i] = True
        return ret

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Solution().ladderLength(beginWord, endWord, wordList)