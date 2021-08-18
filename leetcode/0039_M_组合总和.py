'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
'''
class Solution:
    '''
    排序之后递归, temp存储临时结果
    1. 如果nums为空或者target < nums[0], 返回
    2. 遍历nums:
        nums[i] < target, nums[i]放入temp, 递归调用(nums, target, temp)
        nums[i] == target, nums[i]放入temp, temp放入ret
        nums[i] > target, 结束遍历
    '''
    def combinationSum(self, candidates, target: int):
        ret = []
        def comSum(nums, target, temp):
            if len(nums) and target < nums[0]:
                return
            for num in nums:
                if target > num:
                    t1 = temp.copy()
                    t1.append(num)
                    comSum(nums, target - num, t1)
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

nums = [2,3,6,7]
so = Solution()
print(so.combinationSum(nums, 7))

