'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''
class Solution:
    def generateParenthesis(self, n: int):
        ret = []
        if n == 0:
            return ret
        ret.append('')
        for i in range(n * 2):
            temp = []
            for s in ret:
                if s.count('(') < n:
                    temp.append(s + '(')
                if s.count('(') > s.count(')'):
                    temp.append(s + ')')
            if temp != []:
                ret = temp
            print(ret)
        return ret

so = Solution()
print(so.generateParenthesis(10))