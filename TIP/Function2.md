# Function2

* lambda

```
l = ['Alpha', 'Beta', 'Charlie', 'Delta', 'Echo']

def wordChange(words, func):
        for word in words:
                print(func(word))

func = lambda word : word.upper()

wordChange(l, func)
```
```
ALPHA
BETA
CHARLIE
DELTA
ECHO
```

* Generator
```
def Code():
        yield 'Alpha'
        yield 'Beta'
        yield 'Charlie'

genrator = Code()
print(next(genrator))
print(next(genrator))
print(next(genrator))
```
```
Alpha
Beta
Charlie
```
* Nested Representation
```
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = ['A', 'B', 'C']
value = ['Alpha', 'Beta', 'Charlie']


test = [i for i in arr if i % 2 == 0]
print(test, type(test))
test = {k: y for k, y in zip(key, value)}
print(test, type(test))
test = {i for i in arr if i % 2 == 0}
print(test, type(test))
test = (i for i in range(10) if i % 2 == 0)
for x in test: print(x, end = ' ')
print(type(test))
```
```
[2, 4, 6, 8, 10] <class 'list'>
{'A': 'Alpha', 'B': 'Beta', 'C': 'Charlie'} <class 'dict'>
{2, 4, 6, 8, 10} <class 'set'>
0 2 4 6 8 <class 'generator'>
```

* Variable Scope
```
A = 'Alpha'

def Local():
        A = 'Alphabet'
        print('local : ', locals())
print('global : ', globals())
```

```
local :  {'A': 'Alphabet'}
global :  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000292B4EC6C88>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/Administrator/Desktop/GitHub/Python-Tutorial/test.py', '__cached__': None, 'A': 'Alpha', 'Local': <function Local at 0x00000292B4E71EA0>}
```
