## Network1

* socket transportation

server.py
```
# port 0-1023
# submit port 1024-49151
# dynamic port 49152-65535

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50007))
    s.listen(1)
    while True:
        connect, address = s.accept()
        with connect:
            while True:
                data = connect.recv(1024)
                if not data:
                    break
                print('data : {}, address : {}'.format(data, address))
                connect.sendall(b'Received: ' + data)
```

```
data : b'Hello Has3ong', address : ('127.0.0.1', 58868)
```

client.py

```
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 50007))
    s.sendall(b'Hello Has3ong')
    data = s.recv(1024)
    print(repr(data))
```

```
b'Received: Hello Has3ong'
```

* socket server, http server

```
import http.server
import socketserver

with socketserver.TCPServer(('127.0.0.1', 8000),
                            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
    
# 127.0.0.1:8000
```

* XMLRPC

server.py

```
from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:

    def add(x, y):
        return x  + y

    server.register_function(add, "add")
    server.serve_forever()
```

client.py

```
import xmlrpc.client

with xmlrpc.client.ServerProxy('http://127.0.0.1:8000/') as proxy:
    print(proxy.add(123, 456))
```


* NetowrkX

```
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3])

G.add_edge(1, 2)
G.add_edge(1, 3)

nx.draw(G)
plt.show()
```