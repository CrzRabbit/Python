import sys

#使用了yield关键字，是一个generator
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield  a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)

#一般情况下那不使用next()，会抛出StopIteration异常
# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         sys.exit()

for n in f:
    print(n)

def yanghuitrian(hor):
    ls = [1]
    count = 0
    yield ls
    count += 1
    while count < hor:
        count += 1
        lt = []
        lt.append(1)
        if len(ls) >= 2:
            for n in range(0, len(ls)):
                if n < len(ls) - 1:
                    lt.append(ls[n] + ls[n + 1])
        lt.append(1)
        yield lt
        ls = lt

for l in yanghuitrian(6):
    print(l)