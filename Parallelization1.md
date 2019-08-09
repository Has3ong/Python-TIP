# Parallelization1

* Threading

```
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def work():
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


def sleep():
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


if __name__=='__main__':
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=sleep)
    t1.start()
    t2.start()
    print('started')
```
```
Thread-1: start
started
Thread-2: start
Thread-1: end
Thread-2: end
```

* demon thread

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


def sleep():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__=='__main__':
    t1 = threading.Thread(target=work)
    t1.setDaemon(True)
    t2 = threading.Thread(target=sleep)
    t1.start()
    t2.start()
    print('started')
```
```
Thread-1: start
Thread-2: start
started
Thread-2: end
```
join
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


def sleep():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__=='__main__':
    t1 = threading.Thread(target=work)
    t1.setDaemon(True)
    t2 = threading.Thread(target=sleep)
    t1.start()
    t2.start()
    print('started')
    t1.join()
```

```
Thread-1: start
started
Thread-2: start
Thread-2: end
Thread-1: end
```