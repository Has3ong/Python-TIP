## Database2

* Hbase

```
$ brew install hbase
$ start-hbase.sh
$ hbase shell```


hbase(main):001:0> create 'sns', 'blog'
0 row(s) in 1.5090 seconds

=> Hbase::Table - sns
hbase(main):002:0> put 'sns', 'user1', 'blog:bitcoin', 'blog1'
0 row(s) in 0.0770 seconds

hbase(main):003:0> scan 'sns'
ROW                        COLUMN+CELL
 user1                     column=blog:bitcoin, timestamp=1565250552786, value=blog1
1 row(s) in 0.0290 seconds

hbase(main):004:0> put 'sns', 'user1', 'blog:soccer', 'blog2'
0 row(s) in 0.0160 seconds

hbase(main):005:0> put 'sns', 'user2', 'blog:soccer', 'blog4'
0 row(s) in 0.0120 seconds

hbase(main):006:0> scan 'sns'
ROW                        COLUMN+CELL
 user1                     column=blog:bitcoin, timestamp=1565250552786, value=blog1
 user1                     column=blog:soccer, timestamp=1565250617638, value=blog2
 user2                     column=blog:soccer, timestamp=1565250629855, value=blog4
2 row(s) in 0.0170 seconds

hbase(main):007:0> get 'sns', 'user1'
COLUMN                     CELL
 blog:bitcoin              timestamp=1565250552786, value=blog1
 blog:soccer               timestamp=1565250617638, value=blog2
1 row(s) in 0.0270 seconds

hbase(main):008:0> scan 'sns', {COLUMNS => ['blog:soccer']}
ROW                        COLUMN+CELL
 user1                     column=blog:soccer, timestamp=1565250617638, value=blog2
 user2                     column=blog:soccer, timestamp=1565250629855, value=blog4
2 row(s) in 0.0350 seconds

hbase(main):009:0> scan 'sns'
ROW                        COLUMN+CELL
 user1                     column=blog:bitcoin, timestamp=1565250552786, value=blog1
 user1                     column=blog:soccer, timestamp=1565250617638, value=blog2
 user2                     column=blog:soccer, timestamp=1565250629855, value=blog4
2 row(s) in 0.0160 seconds

hbase(main):010:0> disable 'sns'
drop 0 row(s) in 2.2780 seconds

hbase(main):011:0> drop 'sns'
0 row(s) in 1.2660 seconds

hbase(main):012:0> quit
```
```
$ hbase thrift start

import happybase

connection = happybase.Connection('localhost')
connection.open()

connection.create_table(b'sns', {'blog': dict()})

table = connection.table(b'sns')

table.put(
    b'user1', {
        b'blog:bitcoin': b'user1 about bitcoin',
        b'blog:soccer': b'user1 about soccer'
    }
)
table.put(
    b'user2', {
    b'blog:soccer': b'user2 about soccer'
    }
)

print(list(table.scan))
connection.disable_table(b'sns')
connection.delete_table(b'sns')
```

```
[(b'user1', {b'blog:bitcoin': b'user1 about bitcoin', b'blog:soccer': b'user1 about soccer'}), (b'user2', {b'blog:soccer': b'user2 about soccer'})]
```

* pickle

```
import pickle

data = {
    'a': [1,2,3],
    'b': ('test', 'test2'),
    'c': {'key': 'value'},
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
    
with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
```

```
{'a': [1, 2, 3], 'b': ('test', 'test2'), 'c': {'key': 'value'}}
__
```

data.pickle

```
�}q(Xaq]q(KKKeXbqXtestqXtest2q�qXcq}qXkeyq	Xvalueq
su.
```

