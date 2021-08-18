'''
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。


示例 1：

输入：s = "1 + 1"
输出：2

示例 2：

输入：s = " 2-1 + 2 "
输出：3

示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def calculate(self, s: str) -> int:
        stack = []
        temp = []
        num = ''
        def cal(temp):
            if temp[0] == '+' or temp[0] == '-':
                ret = 0
                op = temp[0]
            else:
                ret = temp[0]
                op = ''
            for i in range(1, len(temp)):
                if temp[i] == '-' or temp[i] == '+':
                    op = temp[i]
                else:
                    if op == '-':
                        ret -= temp[i]
                    if op == '+':
                        ret += temp[i]
            return ret
        for chr in s:
            if '0' <= chr <= '9':
                num += chr
            else:
                if len(num):
                    temp.append(int(num))
                    num = ''
                if chr == '(':
                    stack += temp
                    temp.clear()
                    stack.append('(')
                if chr == '+' or chr == '-':
                    temp.append(chr)
                if chr == ')':
                    temp = [cal(temp)]
                    t = []
                    if stack.__len__():
                        stack.pop()
                    i = len(stack) - 1
                    while i >= 0:
                        if stack[i] != '(':
                            t.append(stack[i])
                            stack.pop()
                        else:
                            break
                        i -= 1
                    t.reverse()
                    temp = t + temp
        if len(num):
            temp.append(int(num))
        return cal(temp)

s = "(1+(4+5+2)-3)+(6+8)"
Solution().calculate(s)