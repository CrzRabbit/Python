class Solution:
    def threeSumClosest(self, nums, target):
        ret = 2 * 3 * (10 ** 3) + 1
        l = len(nums)
        nums.sort()
        for i in range(0, l):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            temp = target - nums[i]
            right = l - 1
            for left in range(i + 1, right):
                if left > i + 1 and nums[left] == nums[left - 1]:
                    continue
                while left + 1 < right and nums[left] + nums[right] > temp:
                    if abs(target - ret) > abs(target - (nums[i] + nums[left] + nums[right])):
                        ret = nums[i] + nums[left] + nums[right]
                    right -= 1
                if left == right:
                    break
                if abs(target - ret) > abs(target - (nums[i] + nums[left] + nums[right])):
                    ret = nums[i] + nums[left] + nums[right]
        return ret

so = Solution()
print(so.threeSumClosest([-1, 2, 1, -4], 1))