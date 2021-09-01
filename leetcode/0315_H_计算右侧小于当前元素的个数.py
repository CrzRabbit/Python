'''
给定一个整数数组 nums，按要求返回一个新数组  counts。数组 counts 有该性质： counts[i] 的值是   nums[i] 右侧小于  nums[i] 的元素的数量。


示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

提示：

0 <= nums.length <= 10^5
-10^4  <= nums[i] <= 10^4
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    线段树
    '''
    @printTime()
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        m = 10 ** 4
        n = m * 2
        tree = [0 for _ in range(n << 1)]
        for i in range(n - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[(i << 1) + 1]
        def update(index, val):
            index += n
            tree[index] += val
            while index > 0:
                left = index
                right = index
                if left % 2 == 0:
                    right += 1
                else:
                    left -= 1
                index >>= 1
                tree[index] = tree[left] + tree[right]
        def query(left, right):
            left += n
            right += n
            sum = 0
            while left <= right:
                if left % 2 == 1:
                    sum += tree[left]
                    left += 1
                if right % 2 == 0:
                    sum += tree[right]
                    right -= 1
                left >>= 1
                right >>= 1
            return sum
        for i in range(len(nums) - 1, -1, -1):
            update(nums[i] + m, 1)
            ans.append(query(0, nums[i] + m - 1))
        ans.reverse()
        return ans
        
nums = [5, 2, 6, 1]
Solution().countSmaller(nums)