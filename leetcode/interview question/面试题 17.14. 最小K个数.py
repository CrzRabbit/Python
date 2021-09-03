'''
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
提示：

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))
'''
import heapq
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        q = []
        for num in arr:
            heapq.heappush(q, num)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(q))
        return ans

arr = [1,3,5,7,2,4,6,8]
k = 4
Solution().smallestK(arr, k)