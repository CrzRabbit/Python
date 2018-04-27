
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def put(self, key, data):
        hashvalue = self.ghash(key, self.size)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data #replace
            else:
                nextslot = self.rehash(hashvalue, self.size)
                while (self.slots[nextslot] != None and
                        self.slots[nextslot] != key):
                    nextslot = self.rehash(nextslot, self.size)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace

    def get(self, key):
        position = self.ghash(key, self.size)

        data = None
        found = False
        stop = False
        starslot = position

        while (self.slots[position] != None and not found
                and not stop):
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == starslot:
                    stop = True
        return data

    def ghash(self, key, size):
        return key % size

    def rehash(self, key, size):
        return (key + 1) % size

if __name__ == '__main__':
    H = HashTable(4)
    H[23] = '王江川'
    H[47] = '王永林'
    H[16] = '刘波'
    H[79] = '童文芬'

    print(H.slots)
    print(H.data)

    print(H[23])
    print(H[47])