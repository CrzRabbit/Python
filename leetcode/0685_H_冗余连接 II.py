'''
在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。

输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。

返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。


示例 1：

输入：edges = [[1,2],[1,3],[2,3]]
输出：[2,3]

示例 2：

输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
输出：[4,1]

提示：

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ui, vi <= n
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    并查集
    '''
    @printTime()
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        fa = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]
        pa = [i for i in range(n + 1)]
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
        tc = None
        te = None
        for edge in edges:
            if pa[edge[1]] != edge[1]:
                te = edge
            else:
                pa[edge[1]] = edge[0]
                if find(edge[0]) == find(edge[1]):
                    tc = edge
                else:
                    merge(edge[0], edge[1])
        if not te:
            return tc
        else:
            if tc:
                return [pa[te[1]], te[1]]
            else:
                return te

edges = [[3,4],[4,1],[1,2],[2,3],[5,1]]
Solution().findRedundantDirectedConnection(edges)