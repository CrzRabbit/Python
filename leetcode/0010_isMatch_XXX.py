import re
class Solution:
    def isMatch_(self, s: str, p: str) -> bool:
        return re.match('^{}$'.format(p), s) != None

    def isMatch(self, s: str, p: str) -> bool:
        ret = [[False for i in range(len(p) + 1)] for i in range(len(s) + 1)]
        ret[0][0] = True
        for i in range(0, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    if self.match(s, p, i, j - 1):
                        ret[i][j] = ret[i - 1][j] | ret[i][j - 1] | ret[i - 1][j - 2]
                    else:
                        ret[i][j] = ret[i][j - 2]
                else:
                    if self.match(s, p, i, j):
                        ret[i][j] = ret[i - 1][j - 1]

        return ret[len(s)][len(p)]

    def match(self, s, p, i, j):
        if i == 0:
            return False
        if p[j - 1] == '.':
            return True
        return s[i - 1] == p[j - 1]


so = Solution()
print(so.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s'))