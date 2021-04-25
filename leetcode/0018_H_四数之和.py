'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [], target = 0
输出：[]

提示：

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        l = len(nums)
        ret = []
        print(nums)
        for first in range(l - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, l - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                     continue
                third = second + 1
                fourth = l - 1
                #print(nums[first], nums[second], nums[third], nums[fourth])
                if (nums[first] + nums[second] + nums[third] + nums[third + 1]) > target:
                    continue
                elif (nums[first] + nums[second] + nums[fourth - 1] + nums[fourth]) < target:
                    continue
                while third < fourth:
                    if (nums[first] + nums[second] + nums[third] + nums[fourth]) > target:
                        fourth -= 1
                        while fourth >= third and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1
                    elif (nums[first] + nums[second] + nums[third] + nums[fourth]) < target:
                        third += 1
                        while fourth >= third and nums[third] == nums[third - 1]:
                            third += 1
                    else:
                        #print(nums[first], nums[second], nums[third], nums[fourth])
                        ret.append([nums[first], nums[second], nums[third], nums[fourth]])
                        fourth -= 1
                        third += 1
                        while fourth >= third and nums[third] == nums[third - 1]:
                            third += 1
                        while fourth >= third and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1
        return ret

so = Solution()
print(so.fourSum([-2,-1,-1,1,1,2,2], 0))