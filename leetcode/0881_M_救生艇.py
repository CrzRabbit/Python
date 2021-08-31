'''
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。


示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：

输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：

输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
'''
import bisect
import heapq
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        vis = [False for i in range(n)]
        people.sort()
        count = 0
        for i in range(n - 1, -1, -1):
            if not vis[i]:
                vis[i] = True
                temp = limit - people[i]
                j = min(i - 1, bisect.bisect_right(people, temp))
                while j >= 0 and temp > 0:
                    if not vis[j] and temp >= people[j]:
                        vis[j] = True
                        break
                    j -= 1
                count += 1
        return count

    @printTime()
    def _1numRescueBoats(self, people: List[int], limit: int) -> int:
        q = []
        count = 0
        pos = -1
        people.sort(reverse=True)
        for p in people:
            if pos == -1 or q[pos] < p:
                count += 1
                if limit - p > 0:
                    pos += 1
                    if pos >= len(q):
                        q.append(limit - p)
                    else:
                        q[pos] = limit - p
            else:
                pos -= 1
        return count

people = [3,2,3,2,2] * 100000
limit = 6
Solution().numRescueBoats(people, limit)
Solution()._1numRescueBoats(people, limit)