class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = ''
        if len(s) <= numRows or numRows == 1:
            return s
        for k in range(numRows):
            i = 0
            j = k
            while j < len(s):
                ret += s[j]
                x = j
                while x == j:
                    if i % 2 == 0:
                        x += (numRows - 1 - k) * 2
                    else:
                        x += k * 2
                    i += 1
                j = x
        return ret

so = Solution()
print(so.convert('AB', 1))