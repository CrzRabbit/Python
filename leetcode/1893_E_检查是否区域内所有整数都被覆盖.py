'''
给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。



示例 1：

输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：true
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。

示例 2：

输入：ranges = [[1,10],[10,20]], left = 21, right = 21
输出：false
解释：21 没有被任何一个区间覆盖。


提示：

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cur = [[left, right]]
        for range in ranges:
            temp = []
            for c in cur:
                if range[0] > c[1] or range[1] < c[0]:
                    temp.append([c[0], c[1]])
                    continue
                elif range[0] == c[1] and c[1] - 1 >= c[0]:
                    temp.append([c[0], c[1] - 1])
                elif c[0] < range[0] < c[1]:
                    temp.append([c[0], range[0] - 1])
                    if range[1] < c[1]:
                        temp.append([range[1] + 1, c[1]])
                else:
                    if range[1] >= c[0] and range[1] < c[1]:
                        temp.append([range[1] + 1, c[1]])
            cur = temp
        return cur.__len__() == 0
    '''
    集合
    '''
    @printTime()
    def _1isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        mem = set()
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                mem.add(i)
        for r in range(left, right + 1):
            if r not in mem:
                return False
        return True

ranges = [[1, 2], [3, 4], [5, 6]]
left = 2
right = 6
Solution().isCovered(ranges, left, right)
Solution()._1isCovered(ranges, left, right)