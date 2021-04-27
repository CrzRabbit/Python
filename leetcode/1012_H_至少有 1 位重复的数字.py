'''
给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数的个数。

示例 1：
输入：20
输出：1
解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

示例 2：
输入：100
输出：10
解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

示例 3：
输入：1000
输出：262

提示：
1 <= N <= 10^9
'''
class Solution:
    '''
    计算没有重复数字的数的数量
    '''
    def numDupDigitsAtMostN(self, N: int) -> int:
        count = N
        nums = '{}'.format(N)
        l = len(nums)
        used = [0 for i in range(10)]
        '''
        使用2324举例:
        '''
        #计算1000 ~ 2324部分
        #i = 0, 计算1000 ~ 1999部分
        #i = 1, 计算2000 ~ 2299部分
        #i = 3, 计算2300 ~ 2319部分
        for i in range(len(nums)):
            num = ord(nums[i]) - 48
            if i == 0:
                #第一位不能取0
                left = 1
            else:
                #第二位开始可以取0
                left = 0
            #i = 0, left = 1, num = 2
            for j in range(left, num):
                if used[j] != 0:
                    continue
                l = len(nums)
                temp = 1
                #i = 0, j = 1, 后面还有l - 1 - i个位置
                #第k位置可选数字的数量为9 - k - i
                for k in range(l - 1 - i):
                    temp *= (9 - k - i)
                count -= temp
            used[num] += 1
            if used[num] > 1:
                break
            if i == l - 1:
                count -= 1
        #计算1 ~ 999的部分
        l = len(nums)
        while l - 1 > 0:
            temp = 1
            for i in range(l - 1):
                if i < 1:
                    temp *= 9
                else:
                    temp *= 9 - i + 1
            count -= temp
            l -= 1
        return count

    def _numDupDigitsAtMostN(self, N: int) -> int:
        count = 0
        rem = {}
        for i in range(N, 0, -1):
            t = i
            temp = {}
            while t > 0:
                if t in rem:
                    count += 1
                    break
                x = t % 10
                if x not in temp:
                    temp[x] = 1
                else:
                    rem[i] = True
                    count += 1
                    break
                t = t // 10
        return count

num = 1234556
so = Solution()
print(so._numDupDigitsAtMostN(num))
print(so.numDupDigitsAtMostN(num))