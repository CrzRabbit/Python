
class BinHeap:

    def __init__(self, list=None):
        self.current_size = len(list) if list else 0
        self.list = list if list else []

    def build_heap(self):
        index = self.current_size // 2 - 1
        while index >= 0:
            self.down(index)
            index -= 1

    def del_min(self):
        ret = self.list[0]
        self.list[0] = self.list[self.current_size - 1]
        self.current_size -= 1
        self.list.pop()
        self.down(0)
        return ret

    def up(self, key):
        parent = key // 2
        while parent >= 0:
            if self.list[key] < self.list[parent]:
                self.list[key] = self.list[key] ^ self.list[parent]
                self.list[parent] = self.list[key] ^ self.list[parent]
                self.list[key] = self.list[key] ^ self.list[parent]
            key = parent
            parent = key // 2

    def down(self, key):
        while key * 2 + 1 < self.current_size:
            mc = self.min_child(key)
            if self.list[key] > self.list[mc]:
                self.list[key] = self.list[key] ^ self.list[mc]
                self.list[mc] = self.list[key] ^ self.list[mc]
                self.list[key] = self.list[key] ^ self.list[mc]
            key = mc

    def insert(self, value):
        self.list.append(value)
        self.current_size += 1
        self.up(self.current_size - 1)

    def min_child(self, key):
        rc = None
        lc = None
        if (key + 1) * 2 < self.current_size:
            rc = key * 2 + 2
        if key * 2 + 1 < self.current_size:
            lc = key * 2 + 1
        if rc:
            return rc if rc < lc else lc
        else:
            return lc

if __name__ == '__main__':
    bh = BinHeap([25, 5, 23 , 99, 85, 5, 8])
    bh.build_heap()
    print(bh.current_size, bh.list)