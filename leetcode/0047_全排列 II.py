'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

提示：
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
class Solution:
    def permuteUnique(self, nums):
        ret = []
        def getPermute(nums, temp):
            if not len(nums):
                ret.append(temp)
                return
            t2 = []
            for i in range(len(nums)):
                if nums[i] not in t2:
                    t2.append(nums[i])
                    t1 = temp.copy()
                    t1.append(nums[i])
                    getPermute(nums[:i] + nums[i + 1:], t1)
        getPermute(nums, [])
        return ret

nums = [1, 1, 2]
so = Solution()
print(so.permuteUnique(nums))