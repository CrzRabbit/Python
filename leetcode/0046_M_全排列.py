'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums):
        ret = []
        def getPermute(nums, temp):
            if not len(nums):
                ret.append(temp)
                return
            for i in range(len(nums)):
                t1 = temp.copy()
                t1.append(nums[i])
                getPermute(nums[:i] + nums[i + 1:], t1)
        getPermute(nums, [])
        return ret

nums = [1,1,2]
so = Solution()
print(so.permute(nums))