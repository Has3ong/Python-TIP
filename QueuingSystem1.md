## QueuingSystem1

* ZeroMQ Push-Pull

server.py

```
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5690")

id = 0

while True:
    id += 1
    socket.send(str(id).encode())
    print("Sent: {}". format(id))
    time.sleep(1)
```

client.py

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5690")

while True:
    message = socket.recv()
    print("Received : {}". format(message.decode()))
```

* ZeroMQ Pub-Sub

server.py

```
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5690")

id = 0

while True:
    id += 1
    socket.send(str(id).encode())
    print("Sent: {}". format(id))
    time.sleep(1)
```

client.py

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b'sub1 : ')
socket.connect("tcp://127.0.0.1:5690")

while True:
    message = socket.recv()
    print("Received : {}". format(message.decode()))
```

* RabbitMQ celery

listen.py

```
import task

result = task.build_server.delay()
print(result)
```

task.py

```
$ celery -A task worker --loglevel=info

import time
import random
import celery

app = celery.Celery(
    'task',
    broker='amqp://guest@localhost',
    backend='amqp://guest@localhost'
)

@app.task
def build_server():
    print('3 seconds')
    time.sleep(3)
    server_id = random.randint(1, 100)
    return server_id
```