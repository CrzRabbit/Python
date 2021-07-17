'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''
class Solution:
    def isValid(self, s: str) -> bool:
        symbol = {')': '(', '}': '{', ']': '['}
        ret = ''
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                ret += s[i]
            elif s[i] == ')' or s[i] == '}' or s[i] == ']':
                if i > 0 and len(ret) > 0 and ret[-1] == symbol[s[i]]:
                    ret = ret[:-1]
                else:
                    return False
            else:
                return False
        if len(ret) == 0:
            return True
        return False

so = Solution()
print(so.isValid('{((())){}}'))