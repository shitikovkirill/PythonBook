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

    def test_multi_params_function(self):

        def get_args_as_list(*args):
            print(args)
            return args

        def get_dictionary_function(**args):
            return args

        self.assertEqual(('one', 'two', 'three'), get_args_as_list('one', 'two', 'three'))
        with self.assertRaises(TypeError):
            get_args_as_list('one', 'two', three='three')

        self.assertEqual({'two': 2, 'one': 1, 'three': 3}, get_dictionary_function(one=1, two=2, three=3))
        with self.assertRaises(TypeError):
            get_dictionary_function({'two': 2, 'one': 1, 'three': 3})

    def test_parameter_transfer(self):
        my_list = ['one', 'two', 'three']

        def add_to_list(arg):
            arg.append('for')

        add_to_list(my_list)
        self.assertEqual(['one', 'two', 'three', 'for'], my_list)

        new_list = [1, 2, 3]

        def change_list(arg):
            arg = ['one', 'two', 'three']

        change_list(new_list)

        self.assertEqual([1, 2, 3], new_list)

    def test_tuple_in_function(self):
        def return_tuple():
            one = 'one'
            two = 'two'
            return one, two
        self.assertEqual(('one', 'two'), return_tuple())


if __name__ == '__main__':
    unittest.main()
