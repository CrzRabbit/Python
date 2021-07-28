from leetcode.tools.time import printTime


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

    '''
    DP
    '''
    @printTime()
    def _1longestPalindrome(self, s: str) -> str:
        ret = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                    continue
                if s[i] == s[j] and (dp[i + 1][j - 1] or i + 1 == j):
                    dp[i][j] = True
                if dp[i][j]:
                    ret = s[i:j + 1] if j + 1 - i > len(ret) else ret
        return ret

st = 'ccd'
so = Solution()
print(so.longestPalindrome('ccd'))