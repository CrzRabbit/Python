'''
按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：

每对相邻的单词之间仅有单个字母不同。
转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，

如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。


示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。

提示：

1 <= beginWord.length <= 7
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有单词 互不相同
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        ret = []
        wordList = [beginWord] + wordList
        n = len(wordList)
        mem = {}
        visit = [False for _ in range(n)]
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
        print(mem)
        def recursion(temp, index):
            if len(ret) == 0 or len(temp) < len(ret[0]):
                print(temp, index, ret)
                for i in mem[index]:
                    if wordList[i] not in temp:
                        t = temp.copy()
                        t.append(wordList[i])
                        recursion(t, i)
                    if wordList[i] == endWord:
                        t = temp.copy()
                        t.append(wordList[i])
                        if len(ret) == 0 or len(t) == len(ret[0]):
                            ret.append(t)
                        elif len(t) < len(ret[0]):
                            ret.clear()
                            ret.append(t)
                        break
        recursion([beginWord], 0)
        return ret


beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
Solution().findLadders(beginWord, endWord, wordList)