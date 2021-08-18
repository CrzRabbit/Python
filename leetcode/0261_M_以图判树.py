'''
给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        fa = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(idx):
            if idx == fa[idx]:
                return fa[idx]
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
            if find(edge[0]) == find(edge[1]):
                return False
            merge(edge[0], edge[1])
        count = 0
        for i in range(n):
            if fa[i] == i:
                count += 1
            if count > 1:
                return False
        return True

n = 5
edges = [[0,1], [0,2], [0,3], [0,4]]
Solution().validTree(5, edges)