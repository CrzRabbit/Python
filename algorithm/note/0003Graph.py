'''
邻接矩阵
'''
class MGraph:
    def __init__(self, n):
        self.mat = [[0 for _ in range(n)] for _ in range(n)]

    def add(self, u, v, w):
        self.mat[u][v] = w
        self.mat[v][u] = w

class Edge:
    def __init__(self, to=0, w=0, next=0):
        self.to = to
        self.w = w
        self.next = next

'''
邻接表
'''
class NTable:
    def __init__(self, n):
        self.edges = [[] for _ in range(n)]

    def add(self, fr, to, w):
        self.edges[fr].append(Edge(to, w))

    def add2(self, u, v, w):
        self.add(u, v, w)
        self.add(v, u, w)

'''
链式前向星
'''
class ChainFS:
    def __init__(self, n):
        self.cnt = 0
        self.edges = [Edge() for _ in range(n)]
        self.head = [0 for _ in range(n)]

    def add(self, fr, to, w):
        self.cnt += 1
        self.edges[self.cnt].to = to
        self.edges[self.cnt].w = w
        self.edges[self.cnt].next = self.head[fr]
        self.head[fr] = self.cnt