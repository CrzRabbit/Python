'''
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

示例 1：
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。

示例 2：
输入：nums = [9], target = 3
输出：0

提示：
1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000

进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？
'''
class Solution:
    '''
    递归，会超时
    '''
    def _combinationSum4(self, nums, target: int) -> int:
        ret = []
        nums = sorted(nums)
        def sum(nums, target, temp):
            for num in nums:
                if num > target:
                    break
                elif num == target:
                    t = temp.copy()
                    t.append(num)
                    ret.append(t)
                else:
                    t = temp.copy()
                    t.append(num)
                    sum(nums, target - num, t)
        sum(nums, target, [])
        print(ret)
        return len(ret)
    '''
    动态规划
    i = 0 ret[0] = 1
    i = nums[0] ret[i] = 1
    i in [nums[0], target + 1] ret[i] = ret[i - nums[0]] + ... + ret[0]
    '''
    def combinationSum4(self, nums, target: int) -> int:
        #初始化为0
        ret = [0 for i in range(target + 1)]
        # 排序nums
        nums = sorted(nums)
        if len(nums) == 0 or nums[0] > target:
            return 0
        ret[0] = 1
        ret[nums[0]] = 1
        #从nums[0] + 1开始遍历
        for i in range(nums[0] + 1, target + 1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    ret[i] += ret[i - nums[j]]
                else:
                    break
        return ret[target]

nums = [1, 2, 3, 4]
so = Solution()
so._combinationSum4(nums, 5)
print(so.combinationSum4(nums, 5))