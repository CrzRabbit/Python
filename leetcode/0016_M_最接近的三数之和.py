'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。


示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''
class Solution:
    def threeSumClosest(self, nums, target):
        ret = 2 * 3 * (10 ** 3) + 1
        l = len(nums)
        nums.sort()
        for i in range(0, l):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            right = l - 1
            left = i + 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                print(nums[i], nums[left], nums[right], temp, ret)
                if temp == target:
                    return temp
                if abs(target - ret) > abs(target - (nums[i] + nums[left] + nums[right])):
                    ret = nums[i] + nums[left] + nums[right]
                if temp > target:
                    right0 = right
                    while right0 > left and nums[right0] == nums[right]:
                        right0 -= 1
                    right = right0
                else:
                    left0 = left
                    while left0 < right and nums[left0] == nums[left]:
                        left0 += 1
                    left = left0
        return ret

so = Solution()
print(so.threeSumClosest([1,2,4,8,16,32,64,128], 82))