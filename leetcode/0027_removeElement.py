class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

so = Solution()
print(so.removeElement([3, 1, 2, 3, 3, 5, 6], 3))