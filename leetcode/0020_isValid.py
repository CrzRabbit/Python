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