'''
给你两个字符串 s 和 t ，请你通过若干次以下操作将字符串 s 转化成字符串 t ：

选择 s 中一个 非空 子字符串并将它包含的字符就地 升序 排序。
比方说，对下划线所示的子字符串进行操作可以由 "14234" 得到 "12344" 。

如果可以将字符串 s 变成 t ，返回 true 。否则，返回 false 。

一个 子字符串 定义为一个字符串中连续的若干字符。


示例 1：

输入：s = "84532", t = "34852"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"84532" （从下标 2 到下标 3）-> "84352"
"84352" （从下标 0 到下标 2） -> "34852"

示例 2：

输入：s = "34521", t = "23415"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"34521" -> "23451"
"23451" -> "23415"

示例 3：

输入：s = "12345", t = "12435"
输出：false

示例 4：

输入：s = "1", t = "2"
输出：false

提示：

s.length == t.length
1 <= s.length <= 105
s 和 t 都只包含数字字符，即 '0' 到 '9' 。
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def isTransformable(self, s: str, t: str) -> bool:
        mem1 = {}
        table1 = [0 for i in range(10)]
        for c in s:
            if c not in mem1:
                mem1[c] = []
            mem1[c].append(table1[:int(c)])
            table1[int(c)] += 1
        mem2 = {}
        table2 = [0 for i in range(10)]
        for c in t:
            if c not in mem2:
                 mem2[c] = []
            mem2[c].append(table2[:int(c)])
            if c not in mem1:
                return False
            else:
                l = len(mem2[c])
                for i in range(len(mem2[c][-1])):
                    if mem2[c][-1][i] < mem1[c][l - 1][i]:
                        return False
            table2[int(c)] += 1
        if table1 != table2:
            return False
        return True

s = "891"
t = "198"
Solution().isTransformable(s, t)