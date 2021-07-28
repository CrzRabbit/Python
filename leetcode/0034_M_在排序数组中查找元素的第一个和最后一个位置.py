'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
'''

class Solution:
    '''
    二分查找
    '''
    def searchRange(self, nums, target: int):
        ret = [-1, -1]
        if target not in nums:
            return ret
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                break
        mid = (left + right) // 2
        for i in range(mid, -1, -1):
            if nums[i] == target:
                ret[0] = i
            else:
                break
        for i in range(mid, len(nums)):
            if nums[i] == target:
                ret[1] = i
            else:
                break
        return ret

nums = [4]
so = Solution()
print(so.searchRange(nums, 4))