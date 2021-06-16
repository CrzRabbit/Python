'''
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

示例 1：
输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。

示例 2：
输入：nums = [1,2,4,8]
输出：[1,2,4,8]

提示：
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
nums 中的所有整数 互不相同
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    遍历 + 记忆化
    '''
    def largestDivisibleSubset(self, nums):
        ret = []
        #先排序
        nums = sorted(nums)
        def sub(nums):
            temps = []
            for num in nums:
                if len(temps) == 0:
                    temps.append([num])
                else:
                    l = len(temps)
                    t2 = []
                    #遍历temps
                    for i in range(l):
                        t = temps[i]
                        #如果能整除最后一个元素，则能整除前面所有元素
                        if num % t[len(t) - 1] == 0:
                            t1 = t.copy()
                            t1.append(num)
                            #记录最长的集合
                            if len(t1) > len(t2):
                                t2 = t1
                    #保存最长的集合
                    if len(t2):
                        temps.append(t2)
            #返回temps中最长的集合
            for i in range(len(temps) - 1):
                if len(temps) > 1 and len(temps[i]) > len(temps[i + 1]):
                    t = temps[i]
                    temps[i] = temps[i + 1]
                    temps[i + 1] = t
            return temps[len(temps) - 1]
        for i in range(len(nums)):
            #如果能被ret[0]整除，以该元素开头的集合肯定小于ret，直接跳过
            if not len(ret) or (len(ret) and nums[i] % ret[0] != 0):
                temp = sub(nums[i:])
                if len(temp) > len(ret):
                    ret = temp
        return ret
    '''
    DP
    '''
    @printTime()
    def _1largestDivisibleSubset(self, nums):
        nums = sorted(nums)
        self.len = len(nums)
        dp = [[] for i in range(self.len)]
        ret = []
        for i in range(self.len):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[j].__len__() + 1 > dp[i].__len__():
                    dp[i] = dp[j].copy()
            dp[i].append(nums[i])
            if dp[i].__len__() > ret.__len__():
                ret = dp[i]
        return ret

nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824]
so = Solution()
print(so.largestDivisibleSubset(nums))
Solution()._1largestDivisibleSubset(nums)