'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''
class Solution:
    '''
    排序之后递归, temp存储临时结果, 递归到的分支记忆化
    1. 如果nums为空或者target < nums[0], 返回
    2. 如果分支在记忆中, 返回
    2. 遍历nums:
        nums[i] < target, nums[i]放入temp, 递归调用(nums[0:i] + nums[i + 1:], target, temp)
        nums[i] == target, nums[i]放入temp, temp不存在于ret放入ret
        nums[i] > target, 结束遍历
    '''
    def combinationSum2(self, candidates, target: int):
        ret = []
        rem = []
        def comSum(nums, target, temp):
            if (nums, target, temp) in rem:
                return
            rem.append((nums, target, temp))
            if len(nums) == 0 or (len(nums) and target < nums[0]):
                return
            for i in range(len(nums)):
                num = nums[i]
                if target > num:
                    t1 = temp.copy()
                    t1.append(num)
                    comSum(nums[0:i] + nums[i + 1:len(nums)], target - num, t1)
                elif target == num:
                    t1 = temp.copy()
                    t1.append(num)
                    t1 = sorted(t1)
                    if t1 not in ret:
                        ret.append(t1)
                else:
                    break
        candidates = sorted(candidates)
        comSum(candidates, target, [])
        return ret

nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
so = Solution()
print(so.combinationSum2(nums, 27))