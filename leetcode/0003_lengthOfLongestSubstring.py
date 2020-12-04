class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        substr = dict()
        head = 0
        for i in range(len(s)):
            if substr.keys().__contains__(s[i]) and substr[s[i]] >= head:
                head = substr[s[i]] + 1
            substr[s[i]] = i
            if i - head + 1 > size:
                size = i - head + 1
        return size

so = Solution()
print(so.lengthOfLongestSubstring("pwwkew"))