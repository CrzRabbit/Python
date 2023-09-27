'''
有效数字（按顺序）可以分成以下几个部分：

一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
小数（按顺序）可以分成以下几个部分：



部分有效数字列举如下：
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
部分无效数字列举如下：
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

示例 1：
输入：s = "0"
输出：true（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字

示例 2：
输入：s = "e"
输出：false

示例 3：
输入：s = "."
输出：false

示例 4：
输入：s = ".1"
输出：true

提示：
1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.'
'''
from leetcode.tools.time import printTime


class Solution:
    def isNumber(self, s: str) -> bool:
        sign = -1
        dot = -1
        e = -1
        num = -1
        for i in range(len(s)):
            l = s[i]
            #当前字符为数字，记录数字位置
            if l >= '0' and l <= '9':
                num = i
            #当前为正负号，记录符号位置
            elif l == '+' or l == '-':
                #如果当前为数字的正负符号，则必须符号，小数点，e/E，数字都要没有出现过
                if sign < 0 and dot < 0 and e < 0 and num < 0:
                    sign = i
                #如果当前为幂的正负符号，则前一个字符必须是e/E
                elif i > 0 and e == i - 1:
                    sign = i
                else:
                    return False
            #当前为小数点，记录小数点的位置
            elif l == '.':
                #当前为小数点的话，必须前面没有小数点，并且没有e/E
                if dot < 0 and e < 0:
                    dot = i
                else:
                    return False
            #当前为e/E，记录位置
            elif l == 'e' or l == 'E':
                #e/E之前必须有数字，并且没有出现过e/E
                if num >= 0 and e < 0:
                    e = i
                else:
                    return False
            else:
                return False
        #e/E后面必须有数字，有小数点就必须有数字，符号后面必须有数字
        if (e >= 0 and e >= num) or (dot >= 0 and num < 0) or (sign >= 0 and sign >= num):
            return False
        return True

s = '-1.1e+30'
so = Solution()
print(so.isNumber(s))