'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 3：
输入：nums = [0]
输出：0

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''
class Solution:
    '''
    依次遍历
    temp[i]为从第0家偷到第i家最多金钱
    temp2[i]为从第0家偷到第i家但是除去第0家的最多金钱
    '''
    def rob(self, nums) -> int:
        ret = {}
        l = len(nums)
        temp = [0] * l
        temp2 = [0] * l
        for i in range(l):
            if i != l - 1:
                if i >= 2:
                    temp[i] = nums[i] + max(temp[:i - 1])
                    temp2[i] = nums[i] + max(temp2[:i - 1])
                else:
                    if i == 0:
                        temp2[i] = 0
                    else:
                        temp2[i] = nums[i]
                    temp[i] = nums[i]
            else:
                if i >= 3:
                    temp[i] = nums[i] + max(temp2[:i - 1])
                else:
                    temp[i] = nums[i]
        return max(temp)

nums = [3,1,2,3,4,5,5]
so = Solution()
print(so.rob(nums))