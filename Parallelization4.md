# Parallelization4

* Pipe

```
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def f(conn):
    conn.send(['test'])
    time.sleep(5)
    conn.close()

if __name__=='__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    p.join()
    logging.debug(child_conn.recv())
```
```
MainProcess: ['test']
```


* Process Transport

server.py

```
import queue
from multiprocessing.managers import BaseManager

queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register(
    'get_queue', callable=lambda: queue
)

manager = QueueManager(
    address=('127.0.0.1', 50000),
    authkey = b'key'
)

server = manager.get_server()
server.serve_forever()
```

client1.py

```
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue')

manager = QueueManager(
    address=('127.0.0.1', 50000),
    authkey = b'key'
)

manager.connect()
queue = manager.get_queue()
queue.put('Hello')
```

client2.py

```
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue')

manager = QueueManager(
    address=('127.0.0.1', 50000),
    authkey = b'key'
)

manager.connect()
queue = manager.get_queue()
print(queue.get())
```