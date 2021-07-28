def print_line(n = 40):
    if n < 0:
        print(40 * '=')
    else:
        print(n * '=')
from datetime import datetime
import time
#直接打印datetime
print('datetime: {0}'.format(datetime))
print_line()
#打印当前时间
print('当前时间: {0}'.format(datetime.now()))
print_line()
#构造一个datetime
print(datetime(2018, 1, 31, 10, 22, 33, 10))
#转换为timestamp
print(datetime().timestamp())
print_line()
