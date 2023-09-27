import os, multiprocessing

def tap(pos):
    while True:
        #time.sleep(0.001)
        os.system('adb shell input tap 500  {}'.format(1000 + pos * 100))

if __name__ == '__main__':
    for i in range(0, 6):
        p = multiprocessing.Process(None, tap, 'tap', (i,))
        p.start()