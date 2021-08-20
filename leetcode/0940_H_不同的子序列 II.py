'''
给定一个字符串 S，计算 S 的不同非空子序列的个数。

因为结果可能很大，所以返回答案模 10^9 + 7.


示例 1：

输入："abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。

示例 2：

输入："aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。

示例 3：

输入："aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。


提示：

S 只包含小写字母。
1 <= S.length <= 2000
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    前缀树思想
    '''
    @printTime()
    def distinctSubseqII(self, s: str) -> int:
        endwidth = [0] * 26
        mode = 10 ** 9 + 7
        for c in s:
            endwidth[ord(c) - ord('a')] = (sum(endwidth) + 1) % mode
        return sum(endwidth) % mode

    @printTime()
    def _1distinctSubseqII(self, s: str) -> int:
        endwidth = [0] * 26
        mode = 10 ** 9 + 7
        temp = 0
        for c in s:
            t = temp + 1 - endwidth[ord(c) - ord('a')] + temp
            endwidth[ord(c) - ord('a')] = temp + 1
            temp = t % mode
        return sum(endwidth) % mode

Solution().distinctSubseqII("abenovehnhobiehobea")
Solution()._1distinctSubseqII("abenovehnhobiehobea")