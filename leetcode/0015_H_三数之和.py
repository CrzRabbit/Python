'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums):
        ret = list()
        l = len(nums)
        nums.sort()
        for i in range(0, l):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            right = l - 1
            for left in range(i + 1, right):
                if left > i + 1 and nums[left] == nums[left - 1]:
                    continue
                while left < right and nums[left] + nums[right] > target:
                    right -= 1
                if left == right:
                    break
                if nums[left] + nums[right] == target:
                    ret.append([nums[i], nums[left], nums[right]])
        return ret

so = Solution()
print(so.threeSum([-1, 1]))