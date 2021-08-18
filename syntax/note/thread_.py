import threading
import queue
import time
import os

exitFlag = 1

class myThread(threading.Thread):
    def __init__(self, threadID, name, queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queue = queue

    def run(self):
        print("开始线程：" + self.name)
        printTime(self.name, self.queue)
        print("结束线程：" + self.name)

def printTime(thread_name, q):
    while exitFlag:
        queueLock.acquire()
        if not q.empty():
            work = q.get()
            print("%s is processing: %s" % (thread_name, work))
            queueLock.release()
        else:
            queueLock.release()
        time.sleep(1)

queueLock = threading.Lock()

nameList = ("Thread-1", "Thread-2", "Thread-3")
workList = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
queue = queue.Queue(10)
threads = []
threadID = 1

for name in nameList:
    thread = myThread(threadID, name, queue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for work in workList:
    queue.put(work)
queueLock.release()

while not queue.empty():
    pass

exitFlag = 0

for thread in threads:
    thread.join()

print("主线程结束")

os.system("pause")
# try:
#     _thread.start_new_thread(printTime,("Thread1", 2))
#     _thread.start_new_thread(printTime,("Thread2", 3))
# except:
#     print("No thread start!")

