class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def buildNext(part):
            next = []
            next.append(-1)
            j = 0
            t = -1
            while j < part.__len__() - 1:
                if t < 0 or part[j] == part[t]:
                    j += 1
                    t += 1
                    if part[j] != part[t]:
                        next.append(t)
                    else:
                        next.append(next[t])
                else:
                    t = next[t]
            print(next)
            return next
        next = buildNext(needle)
        i = 0
        j = 0
        while i < haystack.__len__() and j < needle.__len__():
            if j < 0 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == needle.__len__():
            return i - j
        else:
            return -1

so = Solution()
print(so.strStr('010110114100110156201126574422', '0011001111'))