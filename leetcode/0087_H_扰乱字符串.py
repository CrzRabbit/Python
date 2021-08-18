'''
使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。

提示：
s1.length == s2.length
1 <= s1.length <= 30
s1 和 s2 由小写英文字母组成
'''
class Solution:
    ret = {}
    '''
    递归，使用ret记忆已经比较过的组合
    len(s1) == 1, 返回s1[0] == s2[0]
    len(s1) > 1, 如果s2是s1的扰乱字符串，那么range(1:len(s1))中存在i使得:
    sorted(s1[0:i]) == sorted(s2[0:i]) and sorted(s1[i:]) == sorted(s2[i:]) and s2[0:i]是 s1[0:i]的扰乱字符串 and s2[i:]是s1[i:]的扰乱字符串, 或者:
    sorted(s1[0:i]) == sorted(s2[len(s1) - i:]) and sorted(s1[i:]) == sorted(s2[:i]) and s2[len(s1) - 1:]是s1[0:i]的扰乱字符串 and s2[:i]是s1[i:]的扰乱字符串
    '''
    def isScramble(self, s1: str, s2: str) -> bool:
        l = len(s1)
        if (s1, s2) in Solution.ret:
            return Solution.ret[(s1, s2)]
        if l == 1 and s1[0] == s2[0]:
            Solution.ret[(s1, s2)] = True
            return True
        for i in range(1, l):
            t1 = ''.join(sorted(s1[0:i]))
            t2 = ''.join(sorted(s2[0:i]))
            t3 = ''.join(sorted(s2[l - i:]))
            t4 = ''.join(sorted(s1[i:]))
            t5 = ''.join(sorted(s2[i:]))
            t6 = ''.join(sorted(s2[:l - i]))
            if (t1 == t2 and t4 == t5 and self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:])) \
                or (t1 == t3 and t4 == t6 and self.isScramble(s1[0:i], s2[l - i:]) and self.isScramble(s1[i:], s2[:l - i])):
                Solution.ret[(s1, s2)] = True
                return True
        Solution.ret[(s1, s2)] = False
        return False

so = Solution()
print(so.isScramble("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"))