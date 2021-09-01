'''
珂朵莉树
'''
import bisect


class Node:
    def __init__(self, d):
        self.l = d[0]
        self.r = d[1]
        self.v = d[2]

    def __lt__(self, other):
        return self.l < other.l

    def __str__(self):
        return '[{0}, {1}, {2}]'.format(self.l, self.r, self.v)

class ChthollyTree:
    def __init__(self, data):
        self.tree = []
        for d in data:
            bisect.insort(self.tree, Node(d))

    def merge(self):
        if self.tree.__len__() < 2:
            return
        tree = []
        tn = self.tree[0]
        for node in self.tree:
            if node.v == tn.v:
                tn.r = node.r
            else:
                tree.append(tn)
                tn = node
        tree.append(tn)
        self.tree = tree

    def split(self, pos):
        index = bisect.bisect_left(self.tree, Node([pos, 0, 0]))
        if index != self.tree.__len__() and pos == self.tree[index].l:
            return index
        index -= 1
        l = self.tree[index].l
        r = self.tree[index].r
        v = self.tree[index].v
        self.tree.remove(self.tree[index])
        bisect.insort(self.tree, Node([l, pos - 1, v]))
        bisect.insort(self.tree, Node([pos, r, v]))
        return index + 1

    def assign(self, l, r, v):
        self.split(l)
        self.split(r + 1)
        begin = bisect.bisect_left(self.tree, Node([l, 0, 0]))
        end = bisect.bisect_left(self.tree, Node([r + 1, 0, 0]))
        self.tree = self.tree[:begin] + self.tree[end:]
        bisect.insort(self.tree, Node([l, r, v]))

    def __str__(self):
        ret = ''
        for node in self.tree:
            ret += node.__str__()
            ret += ' '
        return ret