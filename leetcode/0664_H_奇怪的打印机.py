'''
有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

示例 1：
输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。

示例 2：
输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。

提示：
1 <= s.length <= 100
s 由小写英文字母组成
'''
class Solution:
    def split(self, s):
        print(s)
        ret = {}
        if len(s) == 0:
            return [], 0
        left = 0
        temp = s[0]
        i = 1
        for i in range(1, len(s)):
            if s[i] != temp:
                if temp not in ret:
                    ret[temp] = [[left, i]]
                else:
                    ret[temp].append([left, i])
                left = i
                temp = s[i]
        if temp not in ret:
            ret[temp] = [[left, i + 1]]
        else:
            ret[temp].append([left, i + 1])
        ret = sorted(ret.values(), key=lambda x: len(x), reverse=True)
        return ret[0], ret.__len__()

    def strangePrinter(self, s: str) -> int:
        temp, l = self.split(s)
        print(temp, l)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        else:
            ret = 1
            if temp[0][0] > 0:
                ret += self.strangePrinter(s[0: temp[0][0]])
            for i in range(len(temp) - 1):
                ret += self.strangePrinter(s[temp[i][1]: temp[i + 1][0]])
            if temp[len(temp) - 1][1] < len(s):
                ret += self.strangePrinter(s[temp[len(temp) - 1][1]:])
        return ret

s = "tbgtgb"
so = Solution()
print(so.strangePrinter(s))