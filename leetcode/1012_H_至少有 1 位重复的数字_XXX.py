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
    def numDupDigitsAtMostN(self, N: int) -> int:
        if N < 10:
            return N
        count = N
        dic = []
        l = 0
        t = N
        while t > 9:
            l += 1
            dic.append(t % 10)
            t = t // 10
        dic.append(t)
        dic.reverse()

        temp = self.numDupDigitsAtMostN(N % (10 ** l))
        print(N % (10 ** l), temp)
        count -= temp

        temp = dic[0] - 1
        for i in range(len(dic) - 1):
            if i == 0:
                temp *= 9
            else:
                temp *= (9 - i)
        count -= temp

        while l > 0:
            temp = 1
            for i in range(l):
                if i <= 1:
                    temp *= 9
                else:
                    temp *= (9 - i + 1)
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

num = 1100
so = Solution()
print(so._numDupDigitsAtMostN(num))
print(so.numDupDigitsAtMostN(num))