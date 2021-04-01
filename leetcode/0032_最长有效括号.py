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
class Solution:
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
        print(bad)
        max = 0
        for i in range(1, len(bad)):
            if bad[i] - bad[i - 1] - 1 > max:
                max = bad[i] - bad[i - 1] - 1
        return max

so = Solution()
print(so.longestValidParentheses('()(()()'))