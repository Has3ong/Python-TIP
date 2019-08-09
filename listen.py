import unittest

class cal(object):
    def add_num(self, x, y):
        result = x + y
        result *= 2
        return result

class caltest(unittest.TestCase):
    def test_add_num(self):
        test = cal()
        self.assertEqual(test.add_num(1, 1), 5)

if __name__=='__main__':
    unittest.main()