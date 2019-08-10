# Parallelization2

* threading object check
```
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def work():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

if __name__=='__main__':
    threads = []
    for _ in range(5):
        t = threading.Thread(target=work)
        t.setDaemon(True)
        t.start()
        threads.append(t)
    print(threads)
    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()
```

```
Thread-1: start
Thread-2: start
Thread-3: start
Thread-4: start
Thread-5: start
[<Thread(Thread-1, started daemon 123145362558976)>, <Thread(Thread-2, started daemon 123145367814144)>, <Thread(Thread-3, started daemon 123145373069312)>, <Thread(Thread-4, started daemon 123145378324480)>, <Thread(Thread-5, started daemon 123145383579648)>]
<_MainThread(MainThread, started 4627817920)>
Thread-1: end
Thread-3: end
Thread-2: end
Thread-4: end
Thread-5: end
```

* Lock

```
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def work(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    time.sleep(5)
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')

def multi(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i * 2
    logging.debug(d)
    lock.release()
    logging.debug('end')


if __name__=='__main__':
    dict = {'x': 5}
    lock = threading.Lock()
    t1 = threading.Thread(target=work, args=(dict, lock))
    t2 = threading.Thread(target=multi, args=(dict, lock))
    t1.start()
    t2.start()
```
```
Thread-1: start
Thread-2: start
Thread-1: {'x': 6}
Thread-1: end
Thread-2: {'x': 12}
Thread-2: end
```

* Semaphore

```
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def work1(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')
def work2(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')
def work3(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')
def work4(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')
def work5(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

if __name__=='__main__':
    semaphore  = threading.Semaphore(2)
    t1 = threading.Thread(target=work1, args=(semaphore,))
    t2 = threading.Thread(target=work1, args=(semaphore,))
    t3 = threading.Thread(target=work1, args=(semaphore,))
    t4 = threading.Thread(target=work1, args=(semaphore,))
    t5 = threading.Thread(target=work1, args=(semaphore,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
```

```
Thread-1: start
Thread-2: start
Thread-2: end
Thread-1: end
Thread-3: start
Thread-4: start
Thread-3: end
Thread-4: end
Thread-5: start
Thread-5: end
```
