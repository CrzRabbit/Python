'''
给你一个整数数组 nums 和一个整数 target 。
以构造一个 表达
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    递归 + 记忆化
    '''
    def _1findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = dict()
        l = len(nums) - 1
        def find(i, target):
            if (i, target) in mem:
                return mem[(i, target)]
            if i == l:
                count = 0
                if nums[i] == target:
                    count += 1
                if nums[i] == -target:
                    count += 1
                    mem[(i, target)] = count
                return count
            count1 = find(i + 1, target - nums[i])
            count2 = find(i + 1, target + nums[i])
            mem[(i, target)] = count1 + count2
            return mem[(i, target)]
        return find(0, target)
    '''
    深度优先
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = [0 for i in range(len(nums))]
        l = len(nums) - 1
        ret = 0
        cur = 0
        temp = 0
        while True:
            #print(cur, temp, mem)
            if cur < l and cur >= 0:
                if mem[cur] == 0:
                    temp += nums[cur]
                    mem[cur] = 1
                    cur += 1
                elif mem[cur] == 1:
                    temp -= nums[cur]
                    mem[cur] = 2
                    cur += 1
            elif cur < 0:
                break
            else:
                if temp + nums[cur] == target:
                    ret += 1
                if temp - nums[cur] == target:
                    ret += 1
                cur -= 1
                while cur >= 0:
                    if mem[cur] == 2:
                        mem[cur] = 0
                        temp += nums[cur]
                        cur -= 1
                    elif mem[cur] == 1:
                        temp -= nums[cur]
                        break
                    else:
                        cur -= 1
        return ret

nums = [9,28,50,9,34,48,2,50,38,10,5,16,44,5,48,21,38,17,21,49]
so = Solution()

print(so._1findTargetSumWays(nums, 20))

print(so.findTargetSumWays(nums, 20))
