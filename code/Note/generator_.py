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