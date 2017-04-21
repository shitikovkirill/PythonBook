from __future__ import absolute_import
import unittest


class TestExceptionMethods(unittest.TestCase):

    def test_my_exception(self):
        ex = None
        try:
            raise MyError('text')
        except MyError as e:
            ex = e.value

        self.assertEqual('text', ex)



class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if __name__ == '__main__':
    unittest.main()