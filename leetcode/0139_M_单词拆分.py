'''
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dict = set(wordDict)
        mem = {}
        def recursion(s):
            if len(s) == 0:
                return True
            if s in mem:
                return mem[s]
            n = len(s)
            ret = False
            for i in range(n + 1, 0, -1):
                if s[:i] in dict and recursion(s[i:]):
                    ret = True
                    break
            mem[s] = ret
            return ret
        for i in range(n + 1, 0, -1):
            if s[:i] in dict and recursion(s[i:]):
                return True
        return False


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
Solution().wordBreak(s, wordDict)