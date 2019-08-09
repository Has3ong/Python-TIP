# Test1

* Doctest

```
class cal(object):
    def add_num(self, x, y):
        """
        >>> c = cal()
        >>> c.add_num(1, 6)
        4

        >>> c.add_num('1','1')
        """
        result = x + y
        result *= 2
        return result

if __name__=='__main__':
    import doctest
    doctest.testmod()
```
```
**********************************************************************
File "/Users/has3ong/Desktop/GitHub/Python-TIP/listen.py", line 5, in __main__.cal.add_num
Failed example:
    c.add_num(1, 6)
Expected:
    4
Got:
    14
**********************************************************************
File "/Users/has3ong/Desktop/GitHub/Python-TIP/listen.py", line 8, in __main__.cal.add_num
Failed example:
    c.add_num('1','1')
Expected nothing
Got:
    '1111'
**********************************************************************
1 items had failures:
   2 of   3 in __main__.cal.add_num
***Test Failed*** 2 failures.
```

* UnitTest

```
import unittest

class cal(object):
    def add_num(self, x, y):
        result = x + y
        result *= 2
        return result

class caltest(unittest.TestCase):
    def test_add_num(self):
        test = cal()
        self.assertEqual(test.add_num(1, 1), 4)

if __name__=='__main__':
    unittest.main()
```

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

F
======================================================================
FAIL: test_add_num (__main__.caltest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/has3ong/Desktop/GitHub/Python-TIP/listen.py", line 12, in test_add_num
    self.assertEqual(test.add_num(1, 1), 5)
AssertionError: 4 != 5

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```
