'''
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。



示例 1：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true

示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true


提示：

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1、s2、和 s3 都由小写英文字母组成
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    递归
    '''
    @printTime()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        mem = {}
        def recursion(s1, s2, s3):
            ret = False
            #print(s3, s1, s2)
            if len(s2) == 0:
                if s1 == s3:
                    ret |= True
                else:
                    ret |= False
            elif len(s1) > len(s3):
                ret |= False
            else:
                if (s1, s2, s3) in mem:
                    return mem[(s1, s2, s3)]
                i = 0
                while i < len(s1):
                    if s1[i] != s3[i]:
                        if i == 0:
                            ret |= False
                        else:
                            ret |= recursion(s2, s1[i:], s3[i:])
                        break
                    elif i + 1 < len(s3) and s3[i + 1] == s2[0]:
                        ret |= recursion(s2, s1[i + 1:], s3[i + 1:])
                    i += 1
                if i == len(s1) and i < len(s3) and s3[i] == s2[0]:
                    ret |= recursion(s2, '', s3[i:])
                mem[(s1, s2, s3)] = ret
            return ret
        if len(s1) == 0:
            if s2 == s3:
                return True
            else:
                return False
        if len(s2) == 0:
            if s1 == s3:
                return True
            else:
                return False
        ret = False
        i = 0
        while i < len(s1) and i < len(s3):
            if s1[i] != s3[i]:
                if i != 0:
                    ret |= recursion(s2, s1[i:], s3[i:])
                break
            elif i + 1 < len(s3) and s3[i + 1] == s2[0]:
                ret |= recursion(s2, s1[i + 1:], s3[i + 1:])
            i += 1
        if i == len(s1):
            ret |= recursion(s2, '', s3[i:])
        i = 0
        while not ret and i < len(s2) and i < len(s3):
            if s2[i] != s3[i]:
                if i != 0:
                    ret |= recursion(s1, s2[i:], s3[i:])
                break
            elif i + 1 < len(s3) and s3[i + 1] == s1[0]:
                ret |= recursion(s1, s2[i + 1:], s3[i + 1:])
            i += 1
        if i == len(s2):
            ret |= recursion(s1, '', s3[i:])
        return ret

    '''
    递归
    '''
    @printTime()
    def _1isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        mem = {}
        def recursion(s1, s2, s3):
            if (s1, s2, s3) in mem:
                return mem[(s1, s2, s3)]
            ret = False
            if len(s2) == 0:
                if s1 == s3:
                    ret |= True
            elif len(s1) == 0:
                if s2 == s3:
                    ret |= True
            elif len(s1) > len(s3) and len(s2) > len(s3):
                ret |= False
            else:
                i = len(s1)
                while i > 0 and len(s1) < len(s3):
                    if s1[:i] == s3[:i] and s2[0] == s3[i]:
                        ret |= recursion(s1[i:], s2, s3[i:])
                    i -= 1
                i = len(s2)
                while i > 0 and len(s2) < len(s3):
                    if s2[:i] == s3[:i] and s1[0] == s3[i]:
                        ret |= recursion(s2[i:], s1, s3[i:])
                    i -= 1
            mem[(s1, s2, s3)] = ret
            return ret
        ret = recursion(s1, s2, s3)
        return ret
    '''
    DP
    '''
    @printTime()
    def _1isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len2 == 0:
            if s1 != s3:
                return False
            else:
                return True
        elif len1 == 0:
            if s2 != s3:
                return False
            else:
                return True
        elif len1 + len2 != len3:
            return False
        dp = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        dp[0][0] = True
        '''
        dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] or dp[i][j - 1])
        '''
        for i in range(0, len1 + 1):
            for j in range(0, len2 + 1):
                t = i + j - 1
                if i > 0:
                    dp[i][j] |= s1[i - 1] == s3[t] and dp[i - 1][j]
                if not dp[i][j] and j > 0:
                    dp[i][j] |= s2[j - 1] == s3[t] and dp[i][j - 1]
        return dp[len1][len2]

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
s1 = "cabbacccabacbcaabaccacacc"
s2 = "bccacbacabbabaaacbbbbcbbcacc"
s3 = "cbccacabbacabbbaacbcacaaacbbacbcaabbbbacbcbcacccacacc"
Solution().isInterleave(s1, s2, s3)
Solution()._1isInterleave(s1, s2, s3)