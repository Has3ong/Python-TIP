# Parallelization3

* Queue

```
import threading
import time
import logging
import queue

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def work1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug('=====================  END ======================')

if __name__=='__main__':
    q = queue.Queue()
    for i in range(10):
        q.put(i)
    t1 = threading.Thread(target=work1, args=(q,))
    t1.start()
    logging.debug('Queue Tasks are not done')
    q.join()
    logging.debug('Queue Task are Done')
    q.put(None)
    t1.join()
```
```
Thread-1: start
MainThread: Queue Tasks are not done
Thread-1: 0
Thread-1: 1
Thread-1: 2
Thread-1: 3
Thread-1: 4
Thread-1: 5
Thread-1: 6
Thread-1: 7
Thread-1: 8
Thread-1: 9
MainThread: Queue Task are Done
Thread-1: =====================  END ======================
```

* MultiProcess
```
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def work1(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(5)
    logging.debug('end')

def work2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

if __name__ =='__main__':
    i = 5
    t1 = multiprocessing.Process(target=work1, args=(i, ))
    t1.daemon= True
    t2 = multiprocessing.Process(name='Renamed', target=work1, args=(i,))
    t1.start()
    t2.start()
    t2.join()
    t1.join()
```
```
Process-1: start
Process-1: 5
Renamed: start
Renamed: 5
Process-1: end
Renamed: end
```

* Pool

```
import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def work1(i):
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')
    return i

if __name__ =='__main__':
    with multiprocessing.Pool(2) as p:
        p1 = p.apply_async(work1, (10,))
        p2 = p.apply_async(work1, (2, ))
        logging.debug(p1.get())
        logging.debug(p2.get())
```
```
ForkPoolWorker-1: start
ForkPoolWorker-2: start
ForkPoolWorker-1: end
MainProcess: 10
ForkPoolWorker-2: end
MainProcess: 2
```