class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ret = ''
        i = 0
        j = 0
        while True:
            j = 0
            if len(strs) > 0:
                if i >= len(strs[0]):
                    return ret
                else:
                    ret += strs[0][i:i + 1]
            else:
                break
            while j < len(strs):
                if i > len(strs[j]) or ret != strs[j][0:i + 1]:
                    return ret[:-1]
                j += 1
            i += 1
        return ret

so = Solution()
print(so.longestCommonPrefix([]))