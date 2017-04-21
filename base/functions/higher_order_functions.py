from __future__ import absolute_import
import unittest


class TestFunctionMethods(unittest.TestCase):

    def test_filter(self):
        my_list = [10, 6, 7, -1, 0]
        new_list = filter(lambda x: x < 5, my_list)

        self.assertEqual([10, 6, 7, -1, 0], my_list)
        self.assertEqual([-1, 0], list(new_list))

    def test_map(self):
        list1 = [10, 6, 7, -1, 0]
        list2 = [90, 0, -2, 31, 1]
        map_list = map(lambda x, y: x+y, list1, list2)
        self.assertEqual([100, 6, 5, 30, 1], list(map_list))

    def test_reduce(self):
        from functools import reduce
        product = reduce((lambda res, y: res * y), [1, 2, 3, 4])
        self.assertEqual(24, product)

if __name__ == '__main__':
    unittest.main()
