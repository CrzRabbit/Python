class Solution(object):
    def lengthOfLongestSubstring(self, t, s):
        """
        :type s: str
        :rtype: int
        """
        if s.__len__() == 0 or s.__len__() == 1:
            return s.__len__()

        max = 0
        for substr in s.split(s[0]):
            print(t + "-" + substr)
            temp = self.lengthOfLongestSubstring(t + "  ", substr)
            print("{0}{1}".format(t, temp))
            if temp > max:
                max = temp + 1
        return max

so = Solution()
print(so.lengthOfLongestSubstring("", "pwwkew"))

