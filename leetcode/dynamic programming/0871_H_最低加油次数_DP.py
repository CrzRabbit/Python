'''
汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。

假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。

当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

示例 1：
输入：target = 1, startFuel = 1, stations = []
输出：0
解释：我们可以在不加油的情况下到达目的地。

示例 2：
输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：我们无法抵达目的地，甚至无法到达第一个加油站。

示例 3：
输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
[[0,10],[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。

提示：
1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
'''
import heapq
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    递归
    '''
    @printTime()
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        self.len = len(stations)
        self.ret = float('inf')
        def re(tar, sta, index, times):
            if sta >= tar:
                if times < self.ret:
                    self.ret = times
                return
            if index >= self.len or times >= self.len:
                return
            dis = stations[index][0] - stations[index - 1][0] if index > 0 else stations[index][0]
            if dis > sta:
                return
            re(tar - dis, sta - dis + stations[index][1], index + 1, times + 1)
            re(tar - dis, sta - dis, index + 1, times)
        re(target, startFuel, 0, 0)
        return int(self.ret) if self.ret != float('inf') else -1

    '''
    DP + 优先队列
    '''
    @printTime()
    def _1minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        self.len = len(stations)
        cur = startFuel
        if cur >= target:
            return 0
        q = list()
        temp = 0
        for i in range(self.len):
            for j in range(temp, self.len):
                if stations[j][0] <= cur:
                    heapq.heappush(q, -stations[j][1])
                    temp = j + 1
                else:
                    break
            if(len(q)):
                sta = heapq.heappop(q) * -1
                cur += sta
                if cur >= target:
                    return i + 1
            else:
                return -1
        return -1

# target = 1000000000
# startFuel = 145267354
# stations = [[32131797,142290934],[86397166,44642653],[99237057,56978680],[130019011,99649968],[154227249,90514223],[198652959,102942413],[272491487,108474929],[282220105,83721209],[302284128,43151624],[318501736,107636032],[359336452,73807027],[425903682,43078334],[447483572,53751173],[469840976,57311636],[472584505,57629539],[531147470,106487691],[611722638,111485731],[650472592,20105771],[692670691,141572192],[747847056,7972504],[800899205,106134661],[825649709,136473550],[880534339,72135820],[887048383,73776979],[967172408,58930710]]
# target = 1000
# startFuel = 83
# stations = [[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]]
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
Solution().minRefuelStops(target, startFuel, stations)
Solution()._1minRefuelStops(target, startFuel, stations)