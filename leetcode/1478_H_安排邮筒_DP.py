'''
给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。

请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。

答案保证在 32 位有符号整数范围以内。

示例 1：
输入：houses = [1,4,8,10,20], k = 3
输出：5
解释：将邮筒分别安放在位置 3， 9 和 20 处。
每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。

示例 2：
输入：houses = [2,3,5,12,18], k = 2
输出：9
解释：将邮筒分别安放在位置 3 和 14 处。
每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。

示例 3：
输入：houses = [7,4,6,1], k = 1
输出：8

示例 4：
输入：houses = [3,6,14,10], k = 4
输出：0

提示：
n == houses.length
1 <= n <= 100
1 <= houses[i] <= 10^4
1 <= k <= n
数组 houses 中的整数互不相同。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def minDistance(self, houses: List[int], k: int) -> int:
        self.len = len(houses)
        houses = sorted(houses)
        mem1 = {}
        mem2 = {}
        def getDis(left, right):
            if (left, right) in mem2:
                return mem2[(left, right)]
            lo = left
            hi = right
            sum = 0
            while left < right:
                sum += (houses[right] - houses[left])
                left += 1
                right -= 1
            mem2[(lo, hi)] = sum
            return sum
        def dp(n, k):
            if k >= n + 1:
                mem1[(n, k)] = 0
                return 0
            elif k <= 1:
                mem1[(n, k)] = getDis(0, n)
                return getDis(0, n)
            if (n, k) in mem1:
                return mem1[(n, k)]
            min = dp(n - 1, k - 1)
            for i in range(n - 1, -1, -1):
                t = getDis(i, n) + dp(i - 1, k - 1)
                if t < min:
                    min = t
            mem1[(n, k)] = min
            return min
        ret = dp(self.len - 1, k)
        return ret

houses = [2,3,5,12,18]
Solution().minDistance(houses, 2)