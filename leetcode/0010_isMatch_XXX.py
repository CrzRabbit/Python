from leetcode.tools.tool import *
class Solution:
    def _isMatch(self, s: str, p: str) -> bool:
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
                    if match(s, p, i, j - 1):
                        ret[i][j] = ret[i - 1][j] | ret[i][j - 1] | ret[i - 1][j - 2]
                    else:
                        ret[i][j] = ret[i][j - 2]
                else:
                    if match(s, p, i, j):
                        ret[i][j] = ret[i - 1][j - 1]
        printMatrix(ret, s, p)
        return ret[len(s)][len(p)]

    def isMatch(self, s: str, p: str) -> bool:
        pass

so = Solution()
print(so._isMatch('aasdf', 'aas*df'))
print(so.isMatch('aasdf', 'aas*df'))