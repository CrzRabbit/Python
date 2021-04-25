class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

so = Solution()
print(so.removeDuplicates([1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6]))