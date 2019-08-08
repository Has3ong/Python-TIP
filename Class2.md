# Class2

* Abstract Class

```
import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 20:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No Drive')

class Adult(Person):
    def __init__(self, age=20):
        if age >= 20:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print('Drive')

baby = Baby()
adult = Adult()
adult.drive()
baby.drive()
```
```
Drive
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/GitHub/Python-TIP/test.py", line 33, in <module>
    baby.drive()
  File "C:/Users/Administrator/Desktop/GitHub/Python-TIP/test.py", line 19, in drive
    raise Exception('No Drive')
Exception: No Drive
```

* Class Static Method
```
def about(year):
    print('year')

class Person():
    name = 'Mike'

    def __init__(self):
        self.age = 32

    @classmethod
    def Print(cls):
        return  cls.name

    @staticmethod
    def about(year):
        print('about', year)

a = Person()
b = Person

print(a.Print())
print(b.Print())

Person.about(2019)
```
```
Mike
Mike
about 2019
```

* Special method
```
class String(object):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return 'Test Example'
    def __len__(self):
        return len(self.text) * 2
    def __add__(self, word):
        return self.text.lower() + self.text.upper()

word = String('Hello Python')
print(word)
print(len(word))
print(word + word)
```
```
Test Example
24
hello pythonHELLO PYTHON
```