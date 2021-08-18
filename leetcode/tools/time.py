import datetime

def printTime():
    def decorator(func):
        def wrap(*args, **kwargs):
            startTime = datetime.datetime.now()
            print(startTime)
            ret = func(*args, **kwargs)
            endTime = datetime.datetime.now()
            print(endTime)
            print((endTime - startTime))
            print(ret)
        return wrap
    return decorator