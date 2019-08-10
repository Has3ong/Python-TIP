# Asynchronous

* coroutine

```
def f():
    while 1:
        ret = yield 'hello'
        yield ret

g = f()
print(next(g))
print(g.send('plus'))
print(next(g))
print(g.send('python'))
```

```
hello
plus
hello
python
```

* yield from

```
def f_from():
    yield 'Hello'
    yield 'Python'
    yield '!!!'
    return 'End'

def f():
    while 1:
        ret = yield from f_from()
        yield ret

g = f()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
```
```
Hello
Python
!!!
End
Hello
Python
```

* asycnio.coroutine

```
import asyncio
import multiprocessing
import threading
import time

loop = asyncio.get_event_loop()

@asyncio.coroutine
def work():
    print('start')
    yield from asyncio.sleep(2)
    print('stop')

if __name__=='__main__':
    loop.run_until_complete(asyncio.wait([work(), work()]))
    loop.close()
```
```
start
start
stop
stop
```

* using asycnio

```
import asyncio
import aiohttp
import time

loop = asyncio.get_event_loop()

async def hello(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            response = await response.read()
            print(response)
            print(time.time())

loop.run_until_complete(asyncio.wait([
    hello("http://httpbin.org/headers"),
    hello("http://httpbin.org/headers")
]))
```

```
b'{\n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "Python/3.7 aiohttp/3.5.4"\n  }\n}\n'
1565428937.849967
b'{\n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "Python/3.7 aiohttp/3.5.4"\n  }\n}\n'
1565428937.850425
```