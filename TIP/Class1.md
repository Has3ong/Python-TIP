# Class1

* Constructor, ~Constructor

```
class Car():
        def __init__(self):
                print('Initalize')
        def __del__(self):
                print('Delete')

BMW = Car()
print(BMW)
```
```
Initalize
<__main__.Car object at 0x0000014C745EEC88>
Delete
```

* Override
```
class Car():
        def __init__(self):
                print('Car Initalize')
        def __del__(self):
                print('Car Delete')

        def setName(self, name):
                self.name = name

class Benz(Car):
        def __init__(self):
                super().__init__()
                print('Benz Initalize')
BMW = Benz()
print(BMW)
```
```
Car Initalize
Benz Initalize
<__main__.Benz object at 0x0000017B3D78EDA0>
Car Delete
```

* Property
```
class Celsius:
    def __init__(self):
        pass

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

a = Celsius()
a.temperature = 123
print(a.to_fahrenheit())

b = Celsius()
b.temperature = -300
print(b.to_fahrenheit())
```
```
Setting value
Getting value
253.4

Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/GitHub/Python-Tutorial/test.py", line 25, in <module>
    b.temperature = -300
  File "C:/Users/Administrator/Desktop/GitHub/Python-Tutorial/test.py", line 16, in temperature
    raise ValueError("Temperature below -273 is not possible")
ValueError: Temperature below -273 is not possible
```

* Duck Typing

```
class Person():
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 20:
            print('Drive')
        else:
            raise Exception ('No Drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 20:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=20):
        if age >= 20:
            super().__init__(age)
        else:
            raise ValueError

class Car():
    def __init__(self):
        pass
    def ride(self, person):
        person.drive()

baby = Baby()
adult = Adult()
adult.drive()
baby.drive()
```
```
Drive
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/GitHub/Python-TIP/test.py", line 34, in <module>
    baby.drive()
  File "C:/Users/Administrator/Desktop/GitHub/Python-TIP/test.py", line 9, in drive
    raise Exception ('No Drive')
Exception: No Drive
```