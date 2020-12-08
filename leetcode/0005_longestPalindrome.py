class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        sorted_index = sorted(range(len(s)), key=lambda key: self.getLongest(key, s))
        for i in sorted_index:
            ret = self.getPalindrome(ret, i, s)
            print(i, ret)
        return ret
    def getLongest(self, i, s):
        if i >= (len(s) - 1 - i):
            return i
        else:
            return len(s) - 1 - i

    def getPalindrome(self, ret, i, s):
        if i + 1 < int((len(ret) + 1) / 2):
            return ret
        left = i - 1
        right = i + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        if (right - 1 - left) > len(ret):
            ret = s[left + 1:right]
        left = i
        right = i + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        if (right - 1 - left) > len(ret):
            ret = s[left + 1:right]
        return ret

st = 'ccd'
so = Solution()
print(so.longestPalindrome('ccd'))