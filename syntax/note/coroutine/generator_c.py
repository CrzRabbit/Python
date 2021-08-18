#协程，使用generator实现
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] consumed: {0}'.format(n))
        r = '200 OK'

def procducer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        r = c.send(n)
        print('[PRODUCER] consumer returned: {0}'.format(r))
    c.close()

c = consumer()
procducer(c)