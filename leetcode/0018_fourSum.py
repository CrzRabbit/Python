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