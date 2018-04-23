import asyncio, random

@asyncio.coroutine
def stupid_fib(N):
    index = 0
    a = 0
    b = 1
    while True:
        print(b)
        time = random.uniform(0, 0.4)
        print('Stupid fib is running...')
        yield from (asyncio.sleep(time))
        a, b = b, a + b
        index += 1

@asyncio.coroutine
def smart_fib(N):
    index = 0
    a = 0
    b = 1
    while True:
        print(b)
        time = random.uniform(0, 0.2)
        print('Smart fib is running...')
        yield from(asyncio.sleep(time))
        a, b = b, a + b
        index += 1

