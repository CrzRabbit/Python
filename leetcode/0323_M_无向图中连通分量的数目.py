'''
给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。

示例 1:

输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

输出: 2
示例 2:

输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

输出:  1
注意:
你可以假设在 edges 中不会出现重复的边。而且由于所以的边都是无向边，[0, 1] 与 [1, 0]  相同，所以它们不会同时在 edges 中出现。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        fa = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(idx):
            if idx != fa[idx]:
                fa[idx] = find(fa[idx])
            return fa[idx]

        def merge(idx1, idx2):
            fa1 = find(idx1)
            fa2 = find(idx2)
            if rank[fa1] >= rank[fa2]:
                fa[fa2] = fa1
            else:
                fa[fa1] = fa2
            if rank[fa1] == rank[fa2] and fa1 != fa2:
                rank[fa1] += 1
        for edge in edges:
            merge(edge[0], edge[1])
        ret = set()
        for i in range(n):
            ret.add(find(i))
        return ret.__len__()

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
Solution().countComponents(n, edges)