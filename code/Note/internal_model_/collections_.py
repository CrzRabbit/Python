def print_line(n = 40):
    if n < 0:
        print(40 * '=')
    else:
        print(n * '=')
#namedtuple
from collections import namedtuple

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 1, 1)
print(isinstance(c, Circle))
print(isinstance(c, tuple))
print_line()

#deque
from collections import deque

dq = deque(['a', 'b', 'c'])
dq.popleft()
dq.appendleft('A')
print(dq)
print_line()

#defaultdict
from collections import defaultdict

dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'key1'
print(dd['key1'])
print(dd['key2'])
print_line()

#OrderedDict 相比与dict,key为有序
from collections import OrderedDict

dict = dict([('a', 1), ('b', 2), ('c', 3)])
print(dict)#输出为key无序
od = OrderedDict([(1, '1'), (2, '2'), (3, '3')])
print(od)#输出key有序
print_line()

#实现一个FIFO的dict
class FIFODict(OrderedDict):
    def __init__(self, capacity):
        super(OrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0#类似三元表达式
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)#删除最先进入的项
            print('pop: {0}'.format(last))
        if containsKey:
            del self[key]
            print('remove: {0}'.format(key))
        else:
            print('add: {0}'.format(key))
        OrderedDict.__setitem__(self, key, value)

fd = FIFODict(5)
for i in range(10):
    fd[i] = i * i
print(fd)
print_line()

#Counter
from collections import Counter

c = Counter()
for ch in 'wangjiangchuan':
    c[ch] = c[ch] + 1       #计算对应字符串出现的个数
print(c)
print_line()

