'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
'''
class Solution:
    def letterCombinations(self, digits):
        keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        count = 1
        if len(digits) == 0:
            return []
        for i in range(len(digits)):
            count *= len(keypad[digits[i]])
        ret = ['' for i in range(count)]
        for i in range(len(digits)):
            for j in range(count):
                temp = 1
                for k in range(i + 1, len(digits)):
                    temp *= len(keypad[digits[k]])
                ret[j] += keypad[digits[i]][int(j / temp) % len(keypad[digits[i]])]
        return ret
so = Solution()
print(so.letterCombinations(''))