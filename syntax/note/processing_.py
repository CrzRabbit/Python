import os

def print_line(n=40):
    print(n * '=')

#print('Process {0} is running...'.format(os.getpid()))
#fork()
# pid = os.fork()
# if pid == 0:#子进程返回0
#     print('I am child process {0} and my parent is {1}...'.format(os.getpid(), os.getppid()))
# else:#父进程返回所创建子进程pid
#     print('I {0} create a process {1}...'.format(os.getppid(), pid))

print_line()

#multiprocessing 启动想要的子进程
from multiprocessing import Process

def test_run(name):
    print('Run child process {0}({1})...'.format(name, os.getpid()))

if __name__ == '__main__':
        print('Process {0} is running...'.format(os.getpid()))
        p = Process(target=test_run, args=('leetcode',))
        p.start()
        p.join()
print_line()

#进程池
from multiprocessing import Pool
import time, random

def long_time_task(name):
    print('Run process {0}...'.format(name))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Process {0} run {1:0.2f} seconds...'.format(name, (end - start)))

print('Parent process {0}'.format(os.getpid()))
p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print('Wait for subprocess done...')
p.close()
p.join()
print('All subprocess done...')
print_line()

#开启其它进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit syntax: {0}'.format(r))
print_line()

#使用communicate控制进程的输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
code, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(code.decode('utf-8'))
print('Exit syntax: {0}'.format(p.returncode))
print_line()

#使用队列进行进程间通信
from multiprocessing import Queue

def write(q):
    print("Write process {0} is running...".format(os.getpid()))
    for c in ['A', 'B', 'C']:
        print('Write {0}...'.format(c))
        q.put(c)
        time.sleep(random.random() * 3)

def read(q):
    print("Read process {0} is running...".format(os.getpid()))
    while True:
        c = q.get(True)
        print('Read {0}...'.format(c))

q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))
pw.start()
pr.start()
pw.join()
print('All work done...')
print_line()