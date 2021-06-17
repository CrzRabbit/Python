'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
'''
from leetcode.tools.matrix import printMatrix
from leetcode.tools.tool import *
class Solution:
    '''
    动态规划
    ret[0][0] = True
    ret[0][?!=0] = False
    p[j - 1] != '*': ret[i][i] |= (p[j - 1] == s[i - 1] and ret[i - 1][j - 1])
    p[j - 1] == '*': 如果字符+星号的组合不匹配s，ret[i][j] = ret[i][j - 2]
                     如果字符+星号的组合匹配s末尾一个或多个字符，必有(s[i - 1] == p[j - 2] and ret[i - 1][j])
    '''
    def isMatch(self, s: str, p: str) -> bool:
        ret = [[False for i in range(len(p) + 1)] for i in range(len(s) + 1)]
        ret[0][0] = True
        def match(s, p, i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
        for i in range(0, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    ret[i][j] |= ret[i][j - 2]
                    if match(s, p, i, j - 1):
                        ret[i][j] |= ret[i - 1][j]
                else:
                    if match(s, p, i, j):
                        ret[i][j] |= ret[i - 1][j - 1]
        printMatrix(ret, s, p)
        return ret[len(s)][len(p)]

    def _1isMatch(self, s: str, p: str) -> bool:
        return re.match('^{}$'.format(p), s) != None
    '''
    递归 + 记忆化
    p[i + 1] == '*' match(s, p) = ((s[0] == p[0] and match(s[1:], p)) or match(s, p[2:])
    p[i + 1] != '*' match(s, p) = s[0] == p[0] and match(s[1:], p[1:])
    '''
    def _3isMatch(self, s: str, p: str) -> bool:
        ret = {}
        def match(s, p):
            if (s, p) in ret:
                return ret[s, p]
            if not p:
                return not s
            first_match = len(s) > 0 and (s[0] == p[0] or p[0] == '.')
            if len(p) >= 2 and p[1] == '*':
                ret[s, p] = (first_match and match(s[1:], p)) or match(s, p[2:])
            else:
                ret[s, p] = first_match and match(s[1:], p[1:])
            return ret[s, p]
        return match(s, p)

s = "aaa"
p = "aaaa"
# s = "mississippi"
# p = "mis*is*p*."
# s = 'aaa'
# p = 'a*a'
so = Solution()
print(so.isMatch(s, p))
print(so._1isMatch(s, p))
print(so._3isMatch(s, p))