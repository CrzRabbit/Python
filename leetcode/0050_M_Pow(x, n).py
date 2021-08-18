'''
实现pow(x, n)，即计算 x 的 n 次幂函数（即，xn）。

示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25

提示：
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''
class Solution:
    '''
    二分 + 记忆化
    '''
    def myPow(self, x: float, n: int) -> float:
        flag = True
        temp = {}
        if n == 0:
            return 1
        if n < 0:
            n *= -1
            flag = False
        def _pow(x, n):
            if (x, n) in temp:
                return temp[(x, n)]
            if n == 1:
                temp[(x, n)] = x
                return x
            i = n // 2
            j = n % 2
            t = _pow(x, i) * _pow(x, i)
            if j:
                t *= x
            temp[(x, n)] = t
            return t
        ret = _pow(x, n)
        if not flag:
            ret = 1 / ret
        return ret

so = Solution()
print(so.myPow(10.000, 13))