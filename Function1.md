# Function1

* Function Parameter
```
def Menu(meal, drink, dessert):
    print('meal = ', meal)
    print('drink = ', drink)
    print('dessert = ', dessert)

Menu('Rice', dessert = 'cake', drink = 'beer')
```
```
meal =  Rice
drink =  beer
dessert =  cake
```

* Default Parameter

```
def Menu(meal='chicken', drink='coke', dessert='cake'):
        print('meal = ', meal)
        print('drink = ', drink)
        print('dessert = ', dessert)

Menu()
```
```
meal =  chicken
drink =  coke
dessert =  cake
```

* Parameter to Tuple, *args

```
def Tuple(*args):
        print(args, type(args))
Tuple('Hello', 'Basic', 'Python')

def Tuple(*args):
        print(args, type(args))

string = ('Basic', 'Python')
Tuple('Hello', *string)
```
```
('Hello', 'Basic', 'Python') <class 'tuple'>
```
* Parameter to Dictionary, **kwargs
```
def Dict(**kwargs):
        print(kwargs, type(kwargs))

Dict(A = 'Alpha', B = 'Beta', C = 'Charlie')

def Dict(**kwargs):
        print(kwargs, type(kwargs))

Dict(A = 'Alpha', B = 'Beta', C = 'Charlie')
```

```
{'A': 'Aplha', 'B': 'Beta', 'C': 'Charile'} <class 'dict'>
```

* Inner Function

```
def outer(a, b):
        def inner(c, d):
                return c+d
        result = inner(a, b)
        return result

print(outer(1, 2)) # 3
```

* Clousre

```
def outer(a, b):
        def inner():
                return a + b

        return inner

f = outer(1, 2)
ret = f()
print(ret) # 3
```

* Decorator
```
def outer(func):
        print('Outer Start')
        def inner(*args, **kwargs):
                print('Inner Start')
                result = func(*args, **kwargs)
                print('Inner End')
                return result
        print('Outer End')
        return inner

@outer
def add(a, b):
        print('Add')
        return a + b

a = add(1, 2)
print(a)
```
```
Outer Start
Outer End
Inner Start
Add
Inner End
3
```
* Decorator 2
```
def outer(func):
        print('Outer Start')
        def inner(*args, **kwargs):
                print('Inner Start')
                result = func(*args, **kwargs)
                print('Inner End')
                return result
        print('Outer End')
        return inner

def Print(func):
        def inner(*args, **kwargs):
                print('def : ', func.__name__)
                print('args :', args)
                print('kwargs: ', kwargs)
                result = func(*args, **kwargs)
                print('return : ', result)
                return result
        return inner
@Print
@outer
def add(a, b):
        print('Add')
        return a + b

a = add(1, 2)
print(a)
```
```
Outer Start
Outer End
def :  inner
args : (1, 2)
kwargs:  {}
Inner Start
Add
Inner End
return :  3
3
```