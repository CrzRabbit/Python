class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ret = '{}'.format(x)
        ret1 = ret[::-1]
        return ret == ret1

so = Solution()
print(so.isPalindrome(-1))