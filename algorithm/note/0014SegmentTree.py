'''
线段树
'''

'''
从根开始更新和查询
'''
class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.tree = [0 for _ in range(self.n << 2)]
        self.mark = [0 for _ in range(self.n << 2)]
        self.build(1, self.n, 1)

    def build(self, l, r, p):
        if l == r:
            self.tree[p] = self.data[l - 1]
            return
        mid = (l + r) >> 1
        self.build(l, mid, p << 1)
        self.build(mid + 1, r, (p << 1) + 1)
        self.tree[p] = self.tree[p << 1] + self.tree[(p << 1) + 1]

    def push_down(self, p, len):
        self.mark[p << 1] += self.mark[p]
        self.mark[(p << 1) + 1] += self.mark[p]
        self.tree[p << 1] += self.mark[p] * (len - (len >> 1))
        self.tree[(p << 1) + 1] += self.mark[p] * (len >> 1)
        self.mark[p] = 0

    def update(self, l, r, d):
        def update(l, r, d, cl, cr, p):
            if cl > r or cr < l:
                return
            elif cl >= l and cr <= r:
                self.tree[p] += (cr - cl + 1) * d
                if cr > cl:
                    self.mark[p] += d
            else:
                mid = (cr + cl) >> 1
                self.push_down(p, (cr - cl + 1))
                update(l, r, d, cl, mid, p << 1)
                update(l, r, d, mid + 1, cr, (p << 1) + 1)
                self.tree[p] = self.tree[p << 1] + self.tree[(p << 1) + 1]
        update(l, r, d, 1, self.n, 1)

    def query(self, l, r):
        def query(l, r, cl, cr, p):
            if cl > r or cr < l:
                return 0
            elif cl >= l and cr <= r:
                return self.tree[p]
            else:
                mid = (cl + cr) >> 1
                self.push_down(p, (cr - cl + 1))
                return query(l, r, cl, mid, p << 1) + query(l, r, mid + 1, cr, (p << 1) + 1)
        return query(l, r, 1, self.n, 1)

    def query(self, index):
        return self.query(index, index)

'''
从叶子开始更新和查询
'''
class SegmentTreeS:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0 for _ in range(self.n << 1)]
        self.tree[self.n:] = data
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]

    def supdate(self, index, val):
        index += self.n
        self.tree[index] += val
        while index > 0:
            left = index
            right = index
            if left % 2 == 1:
                left -= 1
            else:
                right += 1
            index >>= 1
            self.tree[index] = self.tree[left] + self.tree[right]

    def update(self, left, right, val):
        for i in range(left, right + 1):
            self.supdate(i, val)

    def query(self, left, right):
        left += self.n
        right += self.n
        sum = 0
        while left <= right:
            if left % 2 == 1:
                sum += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return sum