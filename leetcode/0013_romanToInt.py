class Solution:
    def romanToInt(self, s: str) -> int:
        roman_ch = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        i = 0
        ret = 0
        while i < len(s):
            if i < len(s) - 1 and roman_ch[s[i]] < roman_ch[s[i + 1]]:
                i += 1
                continue
            if i > 0 and roman_ch[s[i - 1]] < roman_ch[s[i]]:
                ret += (roman_ch[s[i]] - roman_ch[s[i - 1]])
                i += 1
                continue
            ret += roman_ch[s[i]]
            i += 1
        return ret

so = Solution()
print(so.romanToInt('MCMXCIX'))