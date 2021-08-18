'''
并查集 - union-find disjoint sets
'''
class UFDSets:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, index):
        if self.fa[index] == index:
            return self.fa[index]
        self.fa[index] = self.find(self.fa[index])
        return self.fa[index]

    def merge(self, index1, index2):
        fa1 = self.find(index1)
        fa2 = self.find(index2)
        if self.rank[fa1] >= self.rank[fa2]:
            self.fa[fa2] = fa1
        else:
            self.fa[fa1] = fa2
        if self.rank[fa1] == self.rank[fa2] and fa1 != fa2:
            self.rank[fa1] += 1