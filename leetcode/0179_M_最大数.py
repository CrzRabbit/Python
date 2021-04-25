'''
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [1]
输出："1"

示例 4：
输入：nums = [10]
输出："10"

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 109
'''
class Solution:
    '''
    对于520和52可以组合为52052和52520，所以52在前面数字更大
    按字符依次比较520和52的时候，当位于520的0时候，52已经结束，这个时候应当继续比较0和52
    '''
    def largestNumber(self, nums) -> str:
        def compare(a, b):
            la = len(a)
            lb = len(b)
            i = 0
            while i < lb and i < la:
                if a[i] < b[i]:
                    return True
                elif a[i] > b[i]:
                    return False
                i += 1
            if la == lb:
                return True
            #短数字作为长数字前缀的时候，应当用长数字的剩余部分与短数字继续进行比较
            if i == lb:
                return compare(a[lb:], b)
            else:
                return compare(a, b[la:])
        ret = ''
        tnums = []
        count = len(nums)
        exchange = True
        for num in nums:
            tnums.append('{}'.format(num))
        while count and exchange:
            exchange = False
            for i in range(count - 1):
                if not compare(tnums[i], tnums[i + 1]):
                    temp = tnums[i]
                    tnums[i] = tnums[i + 1]
                    tnums[i + 1] = temp
                    exchange = True
            ret += tnums[count - 1]
            count -= 1
        i = count
        while i:
            ret += tnums[i - 1]
            i -= 1
        i = 0
        for s in ret:
            if s == '0':
                i += 1
            else:
                break
        if i == len(ret):
            i -= 1
        return ret[i:]

nums = [0,0,0]
so = Solution()
print(so.largestNumber(nums))