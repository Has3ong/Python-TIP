## FuncTools1

* Memoize

```
def memorize(f):
    memo = {}
    def _wrapper(n):
        if n not in memo:
            memo[n] = f(n)
            return memo[n]
        return memo[n]
    return _wrapper

@memorize
def function(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r

for i in range(10):
    print(function(i))

print('==================================')

for i in range(10):
    print(function(i))
```

* functools.lru_cache()

```
import functools

@functools.lru_cache()
def function(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r

for i in range(10):
    print(function(i))

print('==================================')

for i in range(10):
    print(function(i))
```

* functools.wraps

```
import functools

def decorator(f):
    @functools.wraps(f)
    def wrapper():
        """ Wrapper docstring """
        print('wrapper : decorator start')
        return f()
    return wrapper

@decorator
def example():
    """ Exapmle docstring"""
    print('example')

example()

print(example.__doc__)
help(example)
```

```
wrapper : decorator start
example
 Exapmle docstring
Help on function example in module __main__:

example()
    Exapmle docstring
```

* functools.partial

```
import functools

def f(x, y):
    print('f start')
    return x + y
def task(f):
    print('task start')
    print(f())

p = functools.partial(f, 10, 20)
task(p)
```
```
task start
f start
30
```
