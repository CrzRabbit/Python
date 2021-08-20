'''
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。



示例 1：

输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2

示例 2：

输入：times = [[1,2,1]], n = 2, k = 1
输出：1

示例 3：

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1


提示：

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mem1 = {}
        mem2 = {}
        mem3 = {k: 0}
        for time in times:
            if time[0] not in mem1:
                mem1[time[0]] = []
            mem1[time[0]].append(time[1])
            mem2[(time[0], time[1])] = time[2]
        cur = [k]
        while cur.__len__():
            temp = []
            for c in cur:
                if c in mem1:
                    for m in mem1[c]:
                        if m not in mem3 or mem2[(c, m)] + mem3[c] < mem3[m]:
                            temp.append(m)
                            mem3[m] = mem2[(c, m)] + mem3[c]
            cur = temp
        return max([mem3[key] for key in mem3]) if mem3.__len__() == n else -1

times = [[1,2,1],[2,1,3]]
n = 2
k = 2
Solution().networkDelayTime(times, n, k)