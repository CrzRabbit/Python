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