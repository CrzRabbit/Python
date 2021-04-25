'''
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

示例 1：
输入：nums = [1,2,0]
输出：3

示例 2：
输入：nums = [3,4,-1,1]
输出：2

示例 3：
输入：nums = [7,8,9,11,12]
输出：1

提示：
0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
'''
class Solution:
    def firstMissingPositive(self, nums) -> int:
        l = len(nums)
        i = 0
        count = 0
        while i < l and count < l:
            if nums[i] > 0 and (nums[i] - 1) < l and nums[i] != nums[nums[i] - 1]:
                count += 1
                t1 = nums[i]
                nums[i] = nums[t1 - 1]
                nums[t1 - 1] = t1
                if nums[i] != i + 1 and nums[i] > 0 and (nums[i] - 1) < l:
                    continue
            i += 1
        i = 0
        while i < l:
            if i + 1 != nums[i]:
                return i + 1
            i += 1
        return i + 1

nums = [0, 2, 2, 1, 1]
so = Solution()
print(so.firstMissingPositive(nums))
print(nums)