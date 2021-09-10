'''
分块 区间更新查询
'''
import math


class Block:
    def __init__(self, data):
        n = len(data)
        sq = math.sqrt(n)
        self.data = data
        self.st = [0 for _ in range(sq + 1)]
        self.ed = [0 for _ in range(sq + 1)]
        for i in range(1, sq + 1):
            self.st[i] = n // sq * (i - 1) + 1
            self.ed[i] = n // sq * i
        self.ed[sq] = n
        self.bel = [0 for _ in range(n + 1)]
        for i in range(1, sq + 1):
            for j in range(self.st[i], self.ed[i] + 1):
                self.bel[j] = i
        self.size = [0 for _ in range(sq + 1)]
        for i in range(1, sq + 1):
            self.size[i] = self.ed[i] - self.st[i] + 1
        self.sum = [0 for _ in range(sq + 1)]
        for i in range(1, sq + 1):
            for j in range(self.st[i], self.ed[i] + 1):
                self.sum[i] += self.data[j]
        self.mark = [0 for _ in range(sq + 1)]

    def update(self, left, right, val):
        if self.bel[left] == self.bel[right]:
            for j in range(left, right + 1):
                self.data[j] += val
                self.sum[self.bel[left]] += val
        else:
            for j in range(left, self.ed[self.bel[left]] + 1):
                self.data[j] += val
                self.sum[self.bel[left]] += val
            for j in range(self.st[self.bel[right]], right + 1):
                self.data[j] += val
                self.sum[self.bel[right]] += val
            for i in range(self.bel[left] + 1, self.bel[right]):
                self.mark[i] += val
                
    def query(self, left, right):
        s = 0
        if self.bel[left] == self.bel[right]:
            for j in range(left, right + 1):
                s += self.data[j] + self.mark[self.bel[j]]
        else:
            for j in range(left, self.ed[self.bel[left]] + 1):
                s += self.data[j] + self.mark[self.bel[j]]
            for j in range(self.st[self.bel[right]], right + 1):
                s += self.data[j] + self.mark[self.bel[j]]
            for i in range(self.bel[left] + 1, self.bel[right]):
                s += self.sum[i] + self.mark[i] * self.size[i]
        return s