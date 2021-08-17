'''
最短路径
'''
import heapq
import queue


class Floyd:
    def __init__(self, dist):
        self.dist = dist
        self.n = len(dist)
        for k in range(1, self.n + 1):
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])

    def get(self, n):
        return self.dist[1][n]

class BellmanFord:
    def __init__(self, cfs):
        self.cfs = cfs
        self.n = len(self.cfs.head)
        self.m = len(self.cfs.edges)
        self.dist = [float('inf') for i in range(self.n + 1)]
        self.dist[1] = 0
        for j in range(self.n - 1):
            for i in range(self.m):
                self.dist[self.cfs.edges[i].to] = min(self.dist[self.cfs.edges[i].to], self.dist[self.cfs.edges[i].fr] + self.cfs.edges[i].w)

    def get(self, n):
        return self.dist[n]

class SPFA:
    def __init__(self, cfs):
        self.cfs = cfs
        self.n = len(self.cfs.head)
        self.m = len(self.cfs.edges)
        self.dist = [float('inf') for i in range(self.n + 1)]
        self.vis = [False for i in range(self.n + 1)]
        self.dist[1] = 0
        q = queue.Queue()
        q.put(1)
        self.vis[1] = True
        while not q.empty():
            cur = q.get()
            edge = self.cfs.head[cur]
            while edge:
                if self.dist[edge.fr] + edge.w < self.dist[edge.to]:
                    self.dist[edge.to] = self.dist[edge.fr] + edge.w
                    if not self.vis[edge.to]:
                        self.vis[edge.to] = True
                        q.put(edge.to)
                edge = edge.next

    def get(self, n):
        return self.dist[n]

class Dijkstra:
    def __init__(self, cfs):
        self.cfs = cfs
        self.n = len(self.cfs.head)
        self.m = len(self.cfs.edges)
        self.dist = [float('inf') for i in range(self.n + 1)]
        self.vis = [False for i in range(self.n + 1)]
        self.dist[1] = 0
        q = []
        hq = heapq(q)
        hq.heappush(q, [0, 1])
        while q.__len__():
            dis, cur = hq.heappop(q)
            if self.vis[cur]:
                continue
            self.vis[cur] = True
            edge = self.cfs.head[cur]
            while edge:
                self.dist[edge.to] = min(self.dist[edge.to], self.dist[cur] + edge.w)
                if not self.vis(edge.to):
                    hq.heappush(q, [self.dist[edge.to], edge.to])

    def get(self, n):
        return self.dist[n]