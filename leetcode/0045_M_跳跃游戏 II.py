'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

说明:
假设你总是可以到达数组的最后一个位置。
'''
class Solution:
    '''
    ret[i]记录能跳到i的最小步数，初始化为len(nums) - 1
    j in [i + 1, i + 1 + nums[i]], ret[j] = min(ret[j], ret[i] + 1)
    '''
    def jump(self, nums) -> int:
        ret = [(len(nums) - 1) for i in range(len(nums))]
        ret[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, i + 1 + nums[i]):
                if j < len(nums) and ret[i] + 1 < ret[j]:
                    ret[j] = ret[i] + 1
        return ret[len(ret) - 1]

nums = [2, 0, 1, 1]
so = Solution()
print(so.jump(nums))