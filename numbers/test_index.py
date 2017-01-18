from __future__ import absolute_import
import unittest

class TestStringMethods(unittest.TestCase):
    def test_division(self):
        result = 17 / 3
        self.assertEqual(5, result);

        result = 17.0 / 3
        self.assertEqual(5.666666666666667, result);

        result = 17 // 3
        self.assertEqual(5, result);

        result = 17 % 3
        self.assertEqual(2, result);

    def test_involution(self):
        result = 5 ** 2
        self.assertEqual(25, result);


if __name__ == '__main__':
    unittest.main()

