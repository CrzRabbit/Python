'''
种类并查集
'''
class CUnionFind:
    def __init__(self, m, n):
        self.fa = [i for i in range(n * m)]
        self.rank = [1 for i in range(n * m)]

    def find(self, index):
        if self.fa[index] == index:
            return self.fa[index]
        self.fa[index] = self.find(self.fa[index])
        return self.fa[index]

    def query(self, idx1, idx2):
        return self.find(idx1) == self.find(idx2)

    def merge(self, index1, index2):
        fa1 = self.find(index1)
        fa2 = self.find(index2)
        if self.rank[fa1] >= self.rank[fa2]:
            self.fa[fa2] = fa1
        else:
            self.fa[fa1] = fa2
        if self.rank[fa1] == self.rank[fa2] and fa1 != fa2:
            self.rank[fa1] += 1