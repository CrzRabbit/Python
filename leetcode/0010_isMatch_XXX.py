from leetcode.tools.tool import *
class Solution:
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

    # def _2isMatch(self, s: str, p: str) -> bool:
    #     i = 0
    #     j = 0
    #     ispec = -1
    #     jspec = -1
    #     jtemp = []
    #     while i < len(s):
    #         print(i, j, ispec, jspec, jtemp)
    #         if j < len(p) - 1 and p[j + 1] != '*' and (s[i] == p[j] or p[j] == '.'):
    #             i += 1
    #             j += 1
    #         elif j < len(p) - 1 and p[j + 1] == '*':
    #             jspec = j
    #             if ispec < 0:
    #                 ispec = i
    #             jtemp.append(jspec)
    #             j += 2
    #         elif j < len(p) and (s[i] == p[j] or p[j] == '.'):
    #             i += 1
    #             j += 1
    #         elif j < len(p) and ispec >= 0 and (s[i] == p[j] or p[j] == '.'):
    #             i += 1
    #             j += 1
    #         elif ispec >= 0 and (s[ispec] == p[jspec] or p[jspec] == '.'):
    #             ispec += 1
    #             i = ispec
    #             j = jspec + 2
    #         else:
    #             print('error')
    #             print(i, j, ispec, jspec, jtemp)
    #             if len(jtemp):
    #                 t = 0
    #                 found = False
    #                 while t < len(jtemp):
    #                     if s[ispec] == p[jtemp[t]] or p[jtemp[t]] == '.':
    #                         found = True
    #                         ispec += 1
    #                         i = ispec
    #                         j = jtemp[t]
    #                         break
    #                     t += 1
    #                 if found:
    #                     jtemp.clear()
    #                     print('recovery')
    #                     print(i, j, ispec, jspec, jtemp)
    #                     continue
    #             return False
    #     print(i, j, ispec, jspec, jtemp)
    #     while j < len(p) - 1 and p[j + 1] == '*':
    #         j += 2
    #     return j == len(p)
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