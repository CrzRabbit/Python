class Solution:
    def intToRoman(self, num: int) -> str:
        roman_ch = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        ch_index = 0
        dex = 1000
        ret = ''
        while num > 0:
            count = int(num / dex)
            if count > 0 and count <= 3:
                ret += '{}'.format(roman_ch[ch_index]) * count
            elif count == 4:
                ret += '{0}{1}'.format(roman_ch[ch_index], roman_ch[ch_index - 1])
            elif count == 5:
                ret += '{}'.format(roman_ch[ch_index - 1])
            elif count > 5 and count <= 8:
                ret += '{}'.format(roman_ch[ch_index - 1])
                ret += '{}'.format(roman_ch[ch_index]) * (count - 5)
            elif count == 9:
                ret += '{0}{1}'.format(roman_ch[ch_index], roman_ch[ch_index - 2])
            num = num % dex
            dex = int(dex / 10)
            ch_index += 2
        return ret

so = Solution()
print(so.intToRoman(1999))