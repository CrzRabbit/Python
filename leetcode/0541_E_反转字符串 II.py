'''
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"

示例 2：

输入：s = "abcd", k = 2
输出："bacd"

提示：

1 <= s.length <= 104
s 仅由小写英文组成
1 <= k <= 104
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        l = 0
        r = min(k, n)
        ret = ''
        while r <= n:
            for i in range(r - 1, l - 1, -1):
                ret += s[i]
            ret += s[r: min(r + k, n)]
            if r + k >= n:
                break
            else:
                l = r + k
                r = min(r + 2 * k, n)
        return ret

s = "abcdefg"
k = 10
Solution().reverseStr(s, k)