'''
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

示例 1：
输入：columnNumber = 1
输出："A"

示例 2：
输入：columnNumber = 28
输出："AB"

示例 3：
输入：columnNumber = 701
输出："ZY"

示例 4：
输入：columnNumber = 2147483647
输出："FXSHRXW"

提示：
1 <= columnNumber <= 231 - 1
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ''
        while columnNumber > 0:
            temp = columnNumber % 26
            columnNumber //= 26
            if temp != 0:
                ret = chr(64 + temp) + ret
            else:
                ret = 'Z' + ret
                columnNumber -= 1
        return ret

Solution().convertToTitle(701)