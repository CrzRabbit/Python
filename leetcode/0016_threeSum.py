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