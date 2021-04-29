'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
'''
import math
class Solution:
    '''
    left = 0 right = int(sqrt(c)) = 1
    小则左边增 大则右边减 向中间查找
    '''
    def judgeSquareSum(self, c: int) -> bool:
        t = math.sqrt(c)
        if int(t) == t:
            return True
        left = 0
        right = int(t + 1)
        while left <= right:
            print(left, right)
            t = left ** 2 + right ** 2
            if t > c:
                right -= 1
            elif t < c:
                left += 1
            else:
                return True
        return False

so = Solution()
print(so.judgeSquareSum(2))