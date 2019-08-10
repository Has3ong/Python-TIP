# Enum1

* Enum

```
import enum

class Status(enum.Enum):
    A = 1
    Alpha = 1
    B = 2
    C = 3
    D = 4
    E = 5

print(Status.A)
print(repr(Status.A))
print(Status.A.name)
print(Status.A.value)
print(Status(1))
```
```
Status.A
<Status.A: 1>
A
1
Status.A
```

* IntEnum

```
import enum


class Status(enum.IntEnum):
    A = 1
    Alpha = 1
    B = 2
    C = 3
    D = 4
    E = 5

db = {
    'status1': 2,
    'status2': 4,
}

if db['status1'] == Status.B:
    print('B')
```
```
B
```