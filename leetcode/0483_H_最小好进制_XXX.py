'''
对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

示例 1：
输入："13"
输出："3"
解释：13 的 3 进制是 111。

示例 2：
输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。

示例 3：
输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。

提示：
n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。
'''
import math

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        self.len = math.floor(math.sqrt(n))
        for i in range(2, n):
            sum = 1
            temp = 1
            for j in range(1, self.len):
                temp *= i
                sum += temp
                if sum == n:
                    return '{}'.format(i)
                elif sum > n:
                    break
        return '{}'.format(n - 1)
n = "4681000"
Solution().smallestGoodBase(n)