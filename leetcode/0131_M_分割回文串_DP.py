'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]

提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    递归
    '''
    @printTime()
    def partition(self, s: str) -> List[List[str]]:
        self.len = len(s)
        mem1 = [[True for _ in range(self.len)] for _ in range(self.len)]
        for i in range(self.len - 1, - 1, -1):
            for j in range(i + 1, self.len):
                mem1[i][j] = s[i] == s[j] and mem1[i + 1][j - 1]
        mem = {}
        def re(index):
            if index in mem:
                return mem[index]
            ret = []
            for i in range(index, self.len):
                if mem1[index][i]:
                    if i + 1 < self.len:
                        temp = re(i + 1)
                        for t in temp:
                            t1 = [s[index:i + 1]]
                            t1 += t
                            ret.append(t1)
                    else:
                        ret.append([s[index:i + 1]])
            mem[index] = ret
            return ret
        return re(0)
    '''
    DP
    '''
    @printTime()
    def _1partition(self, s: str) -> List[List[str]]:
        self.len = len(s)
        mem = [[True for _ in range(self.len)] for _ in range(self.len)]
        for i in range(self.len - 1, - 1, -1):
            for j in range(i + 1, self.len):
                mem[i][j] = s[i] == s[j] and mem[i + 1][j - 1]
        dp = [[] for _ in range(self.len)]
        dp[0] = [[s[0]]]
        for i in range(1, self.len):
            for j in range(i + 1):
                if mem[j][i]:
                    if j == 0:
                        dp[i].append([s[j:i + 1]])
                        continue
                    for t in dp[j - 1]:
                        t1 = t.copy()
                        t1.append(s[j:i + 1])
                        dp[i].append(t1)
        return dp[-1]

s = 'aabcbaafiwefnpnngplwkenfowfnwoefhnwonegfnfwneoflwegwerghrthrtwhrtth'
Solution().partition(s)
Solution()._1partition(s)