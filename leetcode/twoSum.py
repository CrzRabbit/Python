from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(range(len(nums)), key=lambda key : nums[key])
        print(sorted_nums)
        head = 0
        tail = len(nums) - 1
        sumresult = nums[sorted_nums[head]] + nums[sorted_nums[tail]]
        while sumresult != target:
            if sumresult < target:
                head += 1
            if sumresult > target:
                tail -= 1
            if head > tail:
                return []
            sumresult = nums[sorted_nums[head]] + nums[sorted_nums[tail]]
        return [sorted_nums[head], sorted_nums[tail]]

so = Solution()
print(so.twoSum([2, 9, 8, 1, 6, 7], 3))