import os
from collections import Iterable
from collections import Iterator
#列表生成式
print([d for d in os.listdir(".")])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in "XYZ" for n in "ABC"])

print("==================")
#generator
g = (x * x for x in range(0, 10))
for n in g:
    print(n)

print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("abc", Iterable))
print(isinstance((x for x in range(0, 10)), Iterable))
print("===================")
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("abc", Iterator))
print(isinstance((x for x in range(0, 10)), Iterator))
print("===================")

it = iter("abc")
print(isinstance(it, Iterator))

print(list(x * x for x in range(0, 10)))