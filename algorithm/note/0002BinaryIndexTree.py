'''
树状数组 - Binary Index Tree
'''
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for i in range(n + 1)]

    def lowbit(self, pos):
        return pos & -pos

    def update(self, pos, val):
        while pos <= self.n:
            self.tree[pos] += val
            pos += self.lowbit(pos)

    def query(self, pos):
        ans = 0
        while pos:
            ans += self.tree[pos]
            pos -= self.lowbit(pos)
        return ans

    def query(self, pstart, pend):
        return self.query(pend) - self.query(pstart - 1)