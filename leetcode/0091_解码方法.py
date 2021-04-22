'''
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)
注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
题目数据保证答案肯定是一个 32 位 的整数。

示例 1：
输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2：
输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

示例 3：
输入：s = "0"
输出：0
解释：没有字符映射到以 0 开头的数字。
含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。

示例 4：
输入：s = "06"
输出：0
解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。

提示：
1 <= s.length <= 100
s 只包含数字，并且可能包含前导零。
'''
class Solution:
    '''
    递归
    '''
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        ret = []
        def decode(s, temp):
            if len(s) == 0:
                ret.append(temp)
                return
            if s[0] == '0':
                return
            decode(s[1:], temp + chr(int(s[0]) - 1 + ord('A')))
            if len(s) >= 2 and int(s[0:2]) >= 10 and int(s[0:2]) <= 26:
                decode(s[2:], temp + chr(int(s[0:2]) - 1 + ord('A')))
        decode(s, '')
        print(ret)
        return ret.__len__()
    '''
    根据s[i]的情况从ret[i - 1]和ret[i - 2]计算ret[i]
    '''
    def _numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        ret = [0 for i in range(len(s))]
        ret[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0' and s[i - 1] >= '1' and s[i - 1] <= '2':
                if i > 2:
                    ret[i] = ret[i - 2]
                else:
                    ret[i] = 1
            elif s[i] >= '1' and s[i] <= '9':
                ret[i] = ret[i - 1]
                if int(s[i - 1:i + 1]) >= 10 and int(s[i - 1:i + 1]) <= 26:
                    if i > 1:
                        ret[i] += ret[i - 2]
                    else:
                        ret[i] += 1
            else:
                break
        print(ret)
        return ret[len(ret) - 1]

s = "11111111111111111111111111111111111111111111"
so = Solution()
print(so._numDecodings(s))
print(so.numDecodings(s))