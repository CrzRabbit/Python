'''
匈牙利算法 - Hungarian algorithm
'''
class Hungarian:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.map = [[0 for _ in range(m)] for _ in range(n)]
        self.visited = None
        self.pair = [None for _ in range(m)]

    def add(self, i, j):
        self.map[i][j] = 1

    def match(self, i):
        for j in range(self.m):
            if self.map[i][j] and not self.visited[j]:
                self.visited[j] = True
                if self.pair[j] is None or self.match(self.pair[j]):
                    self.pair[j] = i
                    return True
        return False

    def hungarian(self):
        cnt = 0
        for i in range(self.n):
            self.visited = [False for _ in range(self.m)]
            if self.match(i):
                cnt += 1
        return cnt

hu = Hungarian(4, 4)
hu.add(0, 1)
hu.add(0, 3)
hu.add(1, 1)
hu.add(2, 0)
hu.add(2, 2)
hu.add(3, 3)
print(hu.hungarian())