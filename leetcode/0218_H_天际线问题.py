'''
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。
列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]


示例 1：

输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
解释：
图 A 显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。

示例 2：

输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]


提示：

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings 按 lefti 非递减排序
'''
from typing import List

from leetcode.tools.sortedcontainers import SortedList
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ret = []
        mem = {}
        cur = 0
        temp = 0
        for i in range(buildings[0][0], buildings[-1][1] + 1):
            while cur < len(buildings) and i >= buildings[cur][0]:
                for j in range(buildings[cur][0], buildings[cur][1]):
                    if j not in mem:
                        mem[j] = 0
                    mem[j] = max(mem[j], buildings[cur][2])
                if buildings[cur][1] not in mem:
                    mem[buildings[cur][1]] = 0
                cur += 1
            if i in mem:
                if mem[i] != temp:
                    temp = mem[i]
                    ret.append([i, mem[i]])
        return ret

    @printTime()
    def _1getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ret = []
        mem = {}
        sl = SortedList()
        for b in buildings:
            rb1 = sl.bisect_right([b[0], b[2]])
            if sl.__len__() == 0 or rb1 == 0:
                sl.add([b[0], b[2]])
            else:
                if sl[rb1 - 1][0] == b[0]:
                    sl[rb1 - 1][1] = b[2]
                elif b[2] > sl[rb1 - 1][1]:
                    sl.add([b[0], b[2]])
            if b[1] not in mem:
                mem[b[1]] = b[2]
            else:
                mem[b[1]] = max(mem[b[1]], b[2])
            rb2 = sl.bisect_right([b[1], b[2]])
            if rb2 == sl.__len__() and sl[rb2 - 1][0] != b[1]:
                for k in range(rb2 - 1, rb1 - 1, -1):
                    if sl[k][1] < b[2]:
                        sl[k][1] = b[2]
                    else:
                        break
                sl.add([b[1], 0])
            else:
                if rb2 < sl.__len__():
                    sl.add([b[1], mem[sl[rb2][0]]])
            print(sl)
        temp = 0
        for s in sl:
            if s[1] != temp:
                temp = s[1]
                ret.append(s)
        return ret

buildings = [[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]]
Solution().getSkyline(buildings)
Solution()._1getSkyline(buildings)