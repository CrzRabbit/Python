import random, time, queue
from multiprocessing.managers import BaseManager

#继承自BaseManager的QueueManager
class QueueManager(BaseManager):
    pass
#只注册名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#服务器的地址
srv_addr = '127.0.0.1'
print('Connect to server {0}.'.format(srv_addr))
#设置服务器的地址、端口和验证码
m = QueueManager(address=(srv_addr, 5000), authkey=b'abc')
#连接
m.connect()
#通过网络获取queue
task = m.get_task_queue()
result = m.get_result_queue()
#客户端从服务器获取任务，将结果放入result
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('Run task {0}*{1}...'.format(n, n))
        r = 'Result is {0}.'.format(n * n)
        result.put(r)
    except queue.Empty:
        print('Task queue is empty.')
print('All task done.')