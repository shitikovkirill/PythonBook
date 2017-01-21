from __future__ import absolute_import
import unittest

class TestStringMethods(unittest.TestCase):
    def test_prisvaevanie(self):
        a, b = 0, 1
        self.assertTrue(a == 0)
        self.assertTrue(b == 1)

    def test_not_null(self):
        string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
        non_null = string1 or string2 or string3

        self.assertEqual('Trondheim', non_null)
        self.assertIsNotNone(non_null)