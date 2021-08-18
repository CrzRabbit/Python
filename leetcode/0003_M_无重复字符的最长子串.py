class Solution:
    '''
    滑动窗口 依次记录上次字符出现的位置
    '''
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