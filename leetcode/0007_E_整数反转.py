class Solution:
    def reverse(self, x: int) -> int:
        f = False
        if x < 0:
            f = True
            x = x * -1
        ret = 0
        while x != 0:
            t = x % 10
            x = x // 10
            ret = ret * 10 + t
        if f:
            ret *= -1
        if ret > 2**31 - 1 or ret < 2**31 * -1:
            return 0
        return ret

so = Solution()
print(so.reverse(-123324324234324243))