'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0

提示：
0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    1. 如果 i = '(', i + 1 = ')', i += 2
    2. 否则 i 入栈
    3. 如果 i = ')', 栈顶为’(‘, i 出栈
    4. 否则 i 入栈
    5. 栈中的都是无效括号的位置，间隔就是有效括号的长度，遍历计算间隔最大值
    '''
    def longestValidParentheses(self, s: str) -> int:
        ret = ''
        bad = [0]
        i = 0
        while i < len(s):
            if s[i] == '(' and i + 1 < len(s) and s[i + 1] == ')':
                i += 2
                continue
            if s[i] == '(':
                ret += s[i]
                bad.append(i + 1)
            else:
                if len(ret) and ret[len(ret) - 1] == '(':
                    ret = ret[:-1]
                    bad = bad[:-1]
                else:
                    ret += s[i]
                    bad.append(i + 1)
            i += 1
        bad.append(len(s) + 1)
        max = 0
        for i in range(1, len(bad)):
            if bad[i] - bad[i - 1] - 1 > max:
                max = bad[i] - bad[i - 1] - 1
        return max
    '''
    DP
    '''
    @printTime()
    def _1longestValidParentheses(self, s: str) -> int:
        self.len = s.__len__()
        dp = [0 for i in range(self.len)]
        ret = 0
        for i in range(1, self.len):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                if s[i - 1] == ')':
                    if i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                        if i - 2 - dp[i - 1] >= 0 and s[i - 2 - dp[i - 1]] == ')':
                            dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
                        else:
                            dp[i] = dp[i - 1] + 2
            if dp[i] > ret:
                ret = dp[i]
        print(dp)
        return ret
s = "(()))())("
so = Solution()
print(so.longestValidParentheses(s))
Solution()._1longestValidParentheses(s)