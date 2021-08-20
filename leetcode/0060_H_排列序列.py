'''
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"


提示：

1 <= n <= 9
1 <= k <= n!
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def getPermutation(self, n: int, k: int) -> str:
        ret = ''
        temp = n - 1
        k -= 1
        def getValue(temp):
            ret = 1
            while temp > 0:
                ret *= temp
                temp -= 1
            return ret
        while len(ret) < n:
            t = k // (getValue(temp)) + 1
            for i in range(1, n + 1):
                if not ret.__contains__('{}'.format(i)):
                    t -= 1
                if t == 0:
                    ret += '{}'.format(i)
                    break
            k = k % (getValue(temp))
            temp -= 1
        return ret
n = 9
k = 5000
Solution().getPermutation(n, k)