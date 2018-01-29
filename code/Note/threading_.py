def print_line(n = 40):
    print(n * '=')

import time, threading, random

def loop():
    print('Thread {0} is running...'.format(threading.current_thread().name))
    for n in range(0, 6):
        print('Thread {0} print {1}.'.format(threading.current_thread().name, n))
        time.sleep(random.random())
    print('Thread {0} ended.'.format(threading.current_thread().name))

print('Thread {0} is running...'.format(threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread {0} ended.'.format(threading.current_thread().name))
print_line()

#Lock
balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def ch(n):
    for i in range(100000):
        # change_it(n)
        try:
            l.acquire()#获取锁
            change_it(n)
        finally:
            l.release()#释放锁

l = threading.Lock()
t1 = threading.Thread(target=ch, args=(5,))
t2 = threading.Thread(target=ch, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
print_line()

'''
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁
，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
'''

#ThreadLocal
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello {0}.({1})'.format(std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Jack',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
print_line()

