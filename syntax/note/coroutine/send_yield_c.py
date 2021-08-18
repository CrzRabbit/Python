# import random, time
#
# def stupid_fib(N):
#     index = 0
#     a = 0
#     b = 1
#     while index < N:
#         sleep_sec = yield b
#         print('let me think {0} secs...'.format(sleep_sec))
#         time.sleep(sleep_sec)
#         a, b = b, a + b
#         index += 1
#
# def copy_stupid_fib(N):
#     print('Copy stupid_fib...')
#     await stupid_fib(N)
#     print('Copy end.')
#
# N = 20
# csfib = copy_stupid_fib(N)
# fib_ret = next(csfib)
# while True:
#     print(fib_ret)
#     try:
#         fib_ret = csfib.send(random.uniform(0, 0.5))
#     except StopIteration:
#         exit()
