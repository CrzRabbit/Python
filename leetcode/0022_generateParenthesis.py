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
print(so.generateParenthesis(4))