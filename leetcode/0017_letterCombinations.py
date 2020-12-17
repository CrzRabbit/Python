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