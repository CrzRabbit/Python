import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#获取结果的队列
result_queue = queue.Queue()
#QueueManager继承自BaseManager
class QueueManager(BaseManager):
    pass
#将两个queue都注册到网络上
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
#绑定端口5000, 验证码‘abc’
m = QueueManager(address=('', 5000), authkey=b'abc')

m.start()
#通过网络访问queue对象
task = m.get_task_queue()
result = m.get_result_queue()
#srv将任务放入task，从result获取结果
for i in range(10):
    n = random.randint(0, 10000)
    print('Task put {0}...'.format(n))
    task.put(n)

print('Try to get result...')
for j in range (10):
    try:
        r = result.get(timeout=100)
        print('{0}'.format(r))
    except queue.Empty:
        print('Result is empty.')