'''
给你一个二维数组 tasks ，用于表示 n​​​​​​ 项从 0 到 n - 1 编号的任务。其中 tasks[i] = [enqueueTimei, processingTimei] 意味着第 i​​​​​​​​​​
项任务将会于 enqueueTimei 时进入任务队列，需要 processingTimei 的时长完成执行。

现有一个单线程 CPU ，同一时间只能执行 最多一项 任务，该 CPU 将会按照下述方式运行：

如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。
如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 执行时间最短 的任务开始执行。如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。
一旦某项任务开始执行，CPU 在 执行完整个任务 前都不会停止。
CPU 可以在完成一项任务后，立即开始执行一项新任务。
返回 CPU 处理任务的顺序。

示例 1：
输入：tasks = [[1,2],[2,4],[3,2],[4,1]]
输出：[0,2,3,1]
解释：事件按下述流程运行：
- time = 1 ，任务 0 进入任务队列，可执行任务项 = {0}
- 同样在 time = 1 ，空闲状态的 CPU 开始执行任务 0 ，可执行任务项 = {}
- time = 2 ，任务 1 进入任务队列，可执行任务项 = {1}
- time = 3 ，任务 2 进入任务队列，可执行任务项 = {1, 2}
- 同样在 time = 3 ，CPU 完成任务 0 并开始执行队列中用时最短的任务 2 ，可执行任务项 = {1}
- time = 4 ，任务 3 进入任务队列，可执行任务项 = {1, 3}
- time = 5 ，CPU 完成任务 2 并开始执行队列中用时最短的任务 3 ，可执行任务项 = {1}
- time = 6 ，CPU 完成任务 3 并开始执行任务 1 ，可执行任务项 = {}
- time = 10 ，CPU 完成任务 1 并进入空闲状态

示例 2：
输入：tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
输出：[4,3,2,0,1]
解释：事件按下述流程运行：
- time = 7 ，所有任务同时进入任务队列，可执行任务项  = {0,1,2,3,4}
- 同样在 time = 7 ，空闲状态的 CPU 开始执行任务 4 ，可执行任务项 = {0,1,2,3}
- time = 9 ，CPU 完成任务 4 并开始执行任务 3 ，可执行任务项 = {0,1,2}
- time = 13 ，CPU 完成任务 3 并开始执行任务 2 ，可执行任务项 = {0,1}
- time = 18 ，CPU 完成任务 2 并开始执行任务 0 ，可执行任务项 = {1}
- time = 28 ，CPU 完成任务 0 并开始执行任务 1 ，可执行任务项 = {}
- time = 40 ，CPU 完成任务 1 并进入空闲状态

提示：
tasks.length == n
1 <= n <= 105
1 <= enqueueTimei, processingTimei <= 109
'''
import heapq

from typing import List

class Solution:
    def shiftDown(self, list):
        cur = len(list) - 1
        parent = (cur - 1) >> 1
        while parent >= 0:
            if list[cur] < list[parent]:
                list[cur], list[parent] = list[parent], list[cur]
                cur = parent
                parent = (cur - 1) >> 1
                continue
            break

    def shiftUp(self, list):
        cur = 0
        end = len(list) - 1
        list[cur], list[end] = list[end], list[cur]
        ret = list[end]
        left = (cur << 1) + 1
        while left < end:
            right = left + 1
            if right < end and list[right] < list[left]:
                left = right
            if list[cur] > list[left]:
                list[cur], list[left] = list[left], list[cur]
                cur = left
                left = (cur << 1) + 1
                continue
            break
        return ret[0], ret[1]

    @timeoutexit(5)
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ret = list()
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x: x[0])
        i = 1
        j = 1
        k = 0
        temp = list()
        while len(temp) or k < len(tasks):
            while k < len(tasks) and i >= tasks[k][0]:
                temp.append(tasks[k][1:])
                self.shiftDown(temp)
                k += 1
            if i == j:
                if len(temp):
                    time, index = self.shiftUp(temp)
                    temp = temp[:-1]
                    j += time
                    ret.append(index)
                else:
                    j += 1
            i = j
        return ret

    '''
    leetcode官方题解, 优先队列
    '''
    def _1getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda x: tasks[x][0])

        ans = list()
        # 优先队列
        q = list()
        # 时间戳
        timestamp = 0
        # 数组上遍历的指针
        ptr = 0

        for i in range(n):
            # 如果没有可以执行的任务，直接快进
            if not q:
                timestamp = max(timestamp, tasks[indices[ptr]][0])
            # 将所有小于等于时间戳的任务放入优先队列
            while ptr < n and tasks[indices[ptr]][0] <= timestamp:
                heapq.heappush(q, (tasks[indices[ptr]][1], indices[ptr]))
                ptr += 1
            # 选择处理时间最小的任务
            process, index = heapq.heappop(q)
            timestamp += process
            ans.append(index)
        return ans

    def _2getOrder(self, tasks: List[List[int]]) -> List[int]:
        ret = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x: x[0])
        i = 1
        j = 1
        k = 0
        q = list()
        while q.__len__() or k < len(tasks):
            while k < len(tasks) and i >= tasks[k][0]:
                heapq.heappush(q, tasks[k][1:])
                k += 1
            if i == j:
                if len(q):
                    time, index = heapq.heappop(q)
                    j += time
                    ret.append(index)
                else:
                    j = tasks[0][0]
            i = j
        return ret

tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
#tasks = [[1000000000,1000000000]]
so = Solution()
#print(so._2getOrder(tasks))
print(so._1getOrder(tasks))
print(so.getOrder(tasks))