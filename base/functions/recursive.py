import unittest
import random


def rec(list_parametr):
    if list_parametr:
        print(list_parametr.pop())
        result = rec(list_parametr)
        print('result')
        print(result)
        if not result:
            print('exec')
            result = random.randint(0, 1)
        return result
    return False


class TestFunctionMethods(unittest.TestCase):

    def test_rec(self):
        x = rec([1, 2, 3, 4, 5])
        print('END')
        print(x)


if __name__ == '__main__':
    unittest.main()