'''
稀疏表
'''
import math


class SparseTable:
    def __init__(self, table):
        self.n = len(table)
        self.m = math.ceil(math.log(self.n, 2))
        self.f = [[0 for i in range(self.m + 1)] for i in range(self.n + 1)]
        for i in range(1, self.n + 1):
            self.f[i][0] = table[i - 1]
        for i in range(1, self.m + 1):
            for j in range(1, self.n - 2 ** i + 1):
                self.f[j][i] = max(self.f[j][i - 1], self.f[j + (1 << (i - 1))][i - 1])
        self.mem = [0 for i in range(self.n + 1)]
        for i in range(2, self.n + 1):
            self.mem[i] = self.mem[i // 2] + 1

    def get(self, l, r):
        s = self.mem[r - l + 1]
        return max(self.f[l][s], self.f[r - (1 << s)][s])
