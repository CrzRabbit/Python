'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
'''
from leetcode.tools.tool import *
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        ispec = -1
        jspec = -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                ispec = i
                jspec = j
                j += 1
            elif ispec >= 0:
                ispec += 1
                i = ispec
                j = jspec + 1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

    def _1isMatch(self, s: str, p: str) -> bool:
        ret = [[False for i in range(len(p) + 1)] for i in range(len(s) + 1)]
        ret[0][0] = True
        for i in range(0, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    for k in range(0, i + 1):
                        if ret[k][j - 1] == True:
                            ret[i][j] = True
                            break
                elif p[j - 1] == '?':
                    if i == 0:
                        ret[i][j] = False
                    else:
                        ret[i][j] = ret[i - 1][j - 1]
                else:
                    if i == 0:
                        ret[i][j] = False
                    else:
                        ret[i][j] = ret[i - 1][j - 1] and p[j - 1] == s[i - 1]
        printMatrix(ret, s, p)
        return ret[len(s)][len(p)]

    def _2isMatch(self, s: str, p: str) -> bool:
        ret = {}
        def match(s, p):
            print(s, p)
            if (s, p) in ret:
                return ret[s, p]
            if not p:
                return not s
            first_match = len(s) > 0 and (s[0] == p[0] or p[0] == '?')
            if p[0] == '*':
                ret[s, p] = match(s, p[1:]) or (len(s) > 0 and match(s[1:], p)) or (len(s) > 0 and match(s[1:], p[1:]))
            else:
                ret[s, p] = first_match and match(s[1:], p[1:])
            return ret[s, p]
        return match(s, p)

s = "acdcdb"
p = "a*c?b"
so = Solution()
print(so.isMatch(s, p))
print(so._2isMatch(s, p))
#print(so.isMatch("bababababababaaaababbabbbbabbbaabbbabaaaaaababbbababbbaaaaabbaaabbaabaababbbaaaaaabbbbabbabaababaabbabababaaaaaaabbbababbbbbabaabbbababbbbabbabbabaaaaaaabbabababaaaabaaaabbabaaaababbabaabbaaabbaabaabaabaa", "a*bab*******b*******babb*ba*aa*a*aa***bbbaa***b**aaaabb**bb*ba*aa***bb**baba********a***b*b*a**a******ba"))