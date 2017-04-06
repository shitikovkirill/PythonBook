from __future__ import absolute_import
import unittest


class TestFunctionMethods(unittest.TestCase):
    def test_unpacking(self):
        args = [3, 6]
        range_var = range(*args)
        self.assertEqual(range(3, 6), range_var)

        def parrot(voltage, state='a stiff', action='voom'):
            self.assertEqual('four million', voltage)
            self.assertEqual("bleedin' demised", state)
            self.assertEqual("VOOM", action)

        d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
        parrot(**d)

    def test_args_function(self):
        def add_args(*args):
            return sum(args)

        def run_something_with_args(func, arg1, arg2):
            return func(arg1, arg2)

        print(type(add_args))
        res = run_something_with_args(add_args, 2, 2)
        self.assertEqual(4, res)

if __name__ == '__main__':
    unittest.main()
