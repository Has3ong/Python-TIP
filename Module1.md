# Module 1

* Commandline argsuments
```
$ python test.py argument1 argument2
import sys
print(sys.argv)
```
```
['test.py', 'argument1', 'argument2']
```

* builtins
```
import builtins

builtins.print()

ranking = {
    'A' : 10,
    'B' : 100,
    'C' : 30,
    'D' : 60
}

print(sorted(ranking, key=ranking.get, reverse=True))
```
```
['B', 'D', 'C', 'A']
```

* defaultdict

```
from collections import defaultdict
s = "ewuivybfsdakvnczxhkjfvhewioqyvndosaiuvfnhaiudfv"
d = defaultdict(int)

for c in s:
        d[c] += 1
print(d)
```
```
defaultdict(<class 'int'>, {'e': 2, 'w': 2, 'u': 3, 'i': 4, 'v': 6, 'y': 2, 'b': 1, 'f': 4, 's': 2, 'd': 3, 'a': 3, 'k': 2, 'n': 3, 'c': 1, 'z': 1, 'x': 1, 'h': 3, 'j': 1, 'o': 2, 'q': 1})
```

* Console Color

```
from termcolor import colored
print('test')
print(colored('test', 'red'))
```
```
Help on function colored in module termcolor:

colored(text, color=None, on_color=None, attrs=None)
    Colorize text.
    
    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.
    
    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.
    
    Available attributes:
        bold, dark, underline, blink, reverse, concealed.
    
    Example:
        colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
        colored('Hello, World!', 'green')

None
```