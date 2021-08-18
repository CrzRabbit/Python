'''
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。


示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]

示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ret = []
        fa = {}
        rank = {}
        mem = {}
        def find(str):
            if str == fa[str]:
                return fa[str]
            fa[str] = find(fa[str])
            return fa[str]
        def merge(str1, str2):
            fa1 = find(str1)
            fa2 = find(str2)
            if rank[fa1] >= rank[fa2]:
                fa[fa2] = fa1
            else:
                fa[fa1] = fa2
            if rank[fa1] == rank[fa2] and fa1 != fa2:
                rank[fa1] += 1
        for i in range(len(equations)):
            if equations[i][0] not in fa:
                fa[equations[i][0]] = equations[i][0]
                rank[equations[i][0]] = 1
            if equations[i][1] not in fa:
                fa[equations[i][1]] = equations[i][1]
                rank[equations[i][1]] = 1
            if equations[i][0] not in mem and equations[i][1] not in mem:
                mem[equations[i][0]] = 1
                mem[equations[i][1]] = mem[equations[i][0]] / values[i]
            elif equations[i][0] not in mem:
                mem[equations[i][0]] = mem[equations[i][1]] * values[i]
            elif equations[i][1] not in mem:
                mem[equations[i][1]] = mem[equations[i][0]] / values[i]
            else:
                temp = (mem[equations[i][0]] / values[i]) / mem[equations[i][1]]
                for key in mem.keys():
                    if find(key) == find(equations[i][1]):
                        mem[key] *= temp
            merge(equations[i][0], equations[i][1])
        for qu in queries:
            if qu[0] not in mem or qu[1] not in mem or find(qu[0]) != find(qu[1]):
                ret.append(-1)
            else:
                ret.append(mem[qu[0]] / mem[qu[1]])
        return ret

equations = [["a","b"],["e","f"],["b","e"]]
values = [3.4,1.4,2.3]
queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
Solution().calcEquation(equations, values, queries)