import asyncio, time
import functools

now = lambda : time.time()

async  def do_some_work(x):
    print('Waiting: {0}s...'.format(x))
    await asyncio.sleep(x)
    return 'COMPLATE WITH {}S.'.format(x)

def callback(t, future):
    print('Result: t[{0}] {1}'.format(t, future.result()))

async def main():

    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine4 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine4)
    ]

    for task in tasks:
        print('Task state: {0}'.format(task._state))

    done, pending = await asyncio.wait(tasks)

    for result in done:
        print(result.result())

start = now()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
try:
    loop.run_until_complete(task)
except KeyboardInterrupt:
    #print(asyncio.Task.all_tasks())
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print('TIME: {0}'.format(now() - start))