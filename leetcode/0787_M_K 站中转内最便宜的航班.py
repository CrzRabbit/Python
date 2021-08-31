'''
有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 toi 抵达 pricei。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。


示例 1：

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200
解释:
城市航班图如下

从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。

示例 2：

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500
解释:
城市航班图如下

从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。

提示：

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
航班没有重复，且不存在自环
0 <= src, dst, k < n
src != dst
'''
import queue
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mem1 = [[] for _ in range(n)]
        mem3 = {}
        vis = [[float('inf') for _ in range(k + 2)] for _ in range(n)]
        for f in flights:
            mem1[f[0]].append(f[1])
            mem3[(f[0], f[1])] = f[2]
        q = queue.Queue()
        q.put([0, src, 0])
        ans = float("inf")
        while not q.empty():
            step, cur, price = q.get()
            if cur == dst:
                ans = min(ans, price)
                continue
            if step == k + 1 or price >= ans:
                continue
            for pos in mem1[cur]:
                if price + mem3[(cur, pos)] < vis[pos][step + 1]:
                    vis[pos][step + 1] = price + mem3[(cur, pos)]
                    q.put([step + 1, pos, price + mem3[(cur, pos)]])
        return -1 if ans == float('inf') else ans

    '''
    DP
    '''
    @printTime()
    def _1findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mem1 = [[] for _ in range(n)]
        mem2 = [[] for _ in range(n)]
        mem3 = {}
        for f in flights:
            mem1[f[0]].append(f[1])
            mem2[f[1]].append(f[0])
            mem3[(f[0], f[1])] = f[2]
        dp = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
        for pos in mem1[src]:
            dp[pos][0] = mem3[(src, pos)]
        for i in range(1, k + 1):
            for j in range(n):
                for pos in mem2[j]:
                    dp[j][i]  = min(dp[j][i], dp[pos][i - 1] + mem3[(pos, j)])
        ans = min(dp[dst])
        return -1 if ans == float('inf') else ans

n, edges, src, dst, k = 13, [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]], 10, 1, 10
Solution().findCheapestPrice(n, edges, src, dst, k)
Solution()._1findCheapestPrice(n, edges, src, dst, k)