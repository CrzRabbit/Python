import re, os, time

import threading

def timeoutCallback():
    print("运行超时")

def timeoutexit(interval=5, callback=timeoutCallback):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            t.setDaemon(True)
            t.start()
            t.join(interval)
            if t.is_alive() and callback:
                return threading.Timer(0, callback).start()
            else:
                return
        return wrapper
    return decorator

@timeoutexit(5)
def showNotCompleted():
    os.chdir('..')
    for item in os.listdir('.'):
        if re.search(r'_XXX\.py', item):
            print(item)

if __name__ == '__main__':
    showNotCompleted()