'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
'''
import queue
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    BFS
    '''
    @printTime()
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ret = []
        q = queue.Queue()
        for word in wordDict:
            if word == s:
                ret.append(word)
                continue
            if len(word) <= len(s) and word == s[:len(word)]:
                q.put([word])
        while not q.empty():
            words = q.get()
            temp = ''.join(words)
            for word in wordDict:
                t = temp + word
                if t == s:
                    wp = words.copy()
                    wp.append(word)
                    ret.append(' '.join(wp))
                    continue
                if len(t) <= len(s) and t == s[:len(t)]:
                    wp = words.copy()
                    wp.append(word)
                    q.put(wp)
        return ret

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
Solution().wordBreak(s, wordDict)