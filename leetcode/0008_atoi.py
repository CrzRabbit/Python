import re
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s.split()) > 0:
            s = s.split()[0]
        else:
            return 0
        restr = r'^[-+]?[0-9]+'
        if re.match(restr, s):
            return min(max(int(re.search(restr, s)[0]), 2**31 * -1), 2**31 - 1)
        return 0

so = Solution()
print('     '.split())
print(so.myAtoi('   -1'))