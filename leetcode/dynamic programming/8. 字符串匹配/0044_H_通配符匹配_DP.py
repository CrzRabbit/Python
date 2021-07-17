'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
'''
from leetcode.tools.time import printTime
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        ispec = -1
        jspec = -1
        while i < len(s):
            #匹配上分为三种情况
            #1. 两个字符匹配，继续匹配下一个字符
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            #2. 如果两个字符不匹配，但是p[j]为‘*’，那么标记i和j的位置，继续匹配i和j + 1
            elif j < len(p) and p[j] == '*':
                ispec = i
                jspec = j
                j += 1
            #3. 前两个条件都不满足，但是i标记过，那就只能ispec和jspec匹配
            elif ispec >= 0:
                ispec += 1
                i = ispec
                j = jspec + 1
            #匹配不上
            else:
                return False
        #考虑p末尾多个‘*’的情况
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
    '''
    DP
    '''
    def _1isMatch(self, s: str, p: str) -> bool:
        ret = [[False for i in range(len(p) + 1)] for i in range(len(s) + 1)]
        ret[0][0] = True
        for i in range(0, len(s) + 1):
            for j in range(1, len(p) + 1):
                #如果p[j]为*，那么只要s[0:i]中有一个位置与p[j - 1]能匹配上，那么s[i]和p[j]就能匹配上
                if p[j - 1] == '*':
                    for k in range(0, i + 1):
                        if ret[k][j - 1] == True:
                            ret[i][j] = True
                            break
                #如果p[j]为?,那么只要s[i - 1]和p[j - 1]能匹配上，s[i]和p[j]就能匹配上
                elif p[j - 1] == '?':
                    if i == 0:
                        ret[i][j] = False
                    else:
                        ret[i][j] = ret[i - 1][j - 1]
                #所有的都要匹配上
                else:
                    if i == 0:
                        ret[i][j] = False
                    else:
                        ret[i][j] = ret[i - 1][j - 1] and p[j - 1] == s[i - 1]
        return ret[len(s)][len(p)]
    '''
    递归
    '''
    def _2isMatch(self, s: str, p: str) -> bool:
        ret = {}
        def match(s, p):
            if (s, p) in ret:
                return ret[s, p]
            if not p:
                return not s
            first_match = len(s) > 0 and (s[0] == p[0] or p[0] == '?')
            #如果p的第一个字符为’*‘
            if p[0] == '*':
                #分为三种情况: *不匹配s中任何一个字符，*匹配s中多个字符，*匹配s中一个字符
                ret[s, p] = match(s, p[1:]) or (len(s) > 0 and match(s[1:], p)) or (len(s) > 0 and match(s[1:], p[1:]))
            else:
                #如果p第一个字符不为‘*’, 那就第一个要匹配，后面的也都要匹配
                ret[s, p] = first_match and match(s[1:], p[1:])
            return ret[s, p]
        return match(s, p)

s = "acdcdb"
p = "a*c?b"
so = Solution()
print(so.isMatch(s, p))
print(so._1isMatch(s, p))
print(so._2isMatch(s, p))
Solution()._3isMatch(s, p)
#print(so.isMatch("bababababababaaaababbabbbbabbbaabbbabaaaaaababbbababbbaaaaabbaaabbaabaababbbaaaaaabbbbabbabaababaabbabababaaaaaaabbbababbbbbabaabbbababbbbabbabbabaaaaaaabbabababaaaabaaaabbabaaaababbabaabbaaabbaabaabaabaa", "a*bab*******b*******babb*ba*aa*a*aa***bbbaa***b**aaaabb**bb*ba*aa***bb**baba********a***b*b*a**a******ba"))