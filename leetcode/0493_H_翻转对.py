'''
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def reversePairs(self, nums: List[int]) -> int:
        n = 2 ** 32
        m = len(nums)
        tree = [0 for _ in range(n << 1)]
        for i in range(n - 1, 0, -1):
            tree[i] = tree[i << 1] + tree[(i << 1) + 1]
        def update(index, val):
            index += n
            tree[index] += val
            while index:
                left = index
                right = index
                if left % 2 == 1:
                    left -= 1
                else:
                    right += 1
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
        ans = 0
        for i in range(m - 1, -1, -1):
            ans += query(0, (nums[i] - 1) >> 1)
            update(nums[i], 1)
        return ans

nums = [2,4,3,5,1]
Solution().reversePairs(nums)