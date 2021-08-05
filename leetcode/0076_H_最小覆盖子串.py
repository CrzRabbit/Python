'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。


注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

示例 2：

输入：s = "a", t = "a"
输出："a"

示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。


提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def minWindow(self, s: str, t: str) -> str:
        mem = {}
        for chr in t:
            if chr not in mem:
                mem[chr] = 0
            mem[chr] += 1
        mem1 = {}
        ret = ''
        for index, chr in enumerate(s):
            if chr in mem:
                if chr not in mem1:
                    mem1[chr] = [0]
                mem1[chr].append(index + 1)
                temp = index + 1
                found = True
                for key in mem:
                    if key in mem1 and mem1[key].__len__() - 1 >= mem[key]:
                        temp = min(temp, mem1[key][-(mem[key])])
                    else:
                        found = False
                        break
                if found and (len(ret) == 0 or len(ret) > (index + 1 - temp + 1)):
                    ret = s[temp - 1:index + 1]
        return ret

    @printTime()
    def _1minWindow(self, s: str, t: str) -> str:
        mem = {}
        for chr in t:
            if chr not in mem:
                mem[chr] = 0
            mem[chr] += 1
        mem1 = {}
        r = ''
        ret = ''
        for index, chr in enumerate(s):
            if chr in mem:
                if chr not in mem1:
                    mem1[chr] = [0]
                mem1[chr].append(index + 1)
                temp = index + 1
                found = True
                if len(ret) == 0 or chr == ret[0]:
                    for key in mem:
                        if key in mem1 and mem1[key].__len__() - 1 >= mem[key]:
                            temp = min(temp, mem1[key][-(mem[key])])
                        else:
                            found = False
                            break
                    if found:
                        ret = s[temp - 1:index + 1]
                        r = ret if len(r) == 0 or len(ret) < len(r) else r
        return r

s = "cabwefgewcwaefgcf" * 10000
t = "caef"
Solution().minWindow(s, t)
Solution()._1minWindow(s, t)