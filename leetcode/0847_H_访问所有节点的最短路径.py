'''
存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。

给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。

返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。


示例 1：

输入：graph = [[1,2,3],[0],[0],[0]]
输出：4
解释：一种可能的路径为 [1,0,2,0,3]

示例 2：

输入：graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
输出：4
解释：一种可能的路径为 [0,1,4,2,3]

提示：

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] 不包含 i
如果 graph[a] 包含 b ，那么 graph[b] 也包含 a
输入的图总是连通图
'''
import queue
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    BFS
    '''
    @printTime()
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = queue.Queue()
        visit = [[False for _ in range(1 << n)] for _ in range(n)]
        for i in range(n):
            q.put([i, 1 << i, 0])
            visit[i][1 << i] = True
        ret = 0
        while not q.empty():
            index, mask, dist = q.get()
            if mask == ((1 << n) - 1):
                ret = dist
                break
            for g in graph[index]:
                temp = mask
                temp |= 1 << g
                if not visit[g][temp]:
                    q.put([g, temp, dist + 1])
                    visit[g][temp] = True
        return ret

graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
Solution().shortestPathLength(graph)