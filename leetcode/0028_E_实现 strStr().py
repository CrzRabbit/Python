'''
实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。
'''
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