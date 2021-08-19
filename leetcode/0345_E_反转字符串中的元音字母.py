'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。


示例 1：

输入："hello"
输出："holle"

示例 2：

输入："leetcode"
输出："leotcede"

提示：

元音字母不包含字母 "y" 。
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def reverseVowels(self, s: str) -> str:
        table = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        mem = []
        cnt = 0
        for chr in s:
            if chr in table:
                mem.append(chr)
                cnt += 1
        ret = ''
        for chr in s:
            if chr in table:
                ret += mem[cnt - 1]
                cnt -= 1
            else:
                ret += chr
        return ret

s = "leetcode"
Solution().reverseVowels(s)