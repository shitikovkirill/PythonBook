from __future__ import absolute_import
import unittest

class TestSetsMethods(unittest.TestCase):
    def test_creation(self):
        basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

        self.assertEqual(set(['orange', 'pear', 'banana', 'apple']), basket)
        self.assertTrue('orange' in basket)
        self.assertFalse('crabgrass' in basket)

        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

        self.assertEqual(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'], basket)
        self.assertTrue('orange' in basket)
        self.assertFalse('crabgrass' in basket)

    def test_operations(self):
        a = set('abracadabra')
        b = set('alacazam')

        self.assertEqual(set(['a', 'r', 'b', 'c', 'd']), a)
        self.assertEqual(set(['a', 'z', 'm', 'l', 'c']), b)

        result = a - b # letters in a but not in b

        self.assertEqual({'r', 'd', 'b'}, result)

        result = a | b # letters in either a or b

        self.assertEqual({'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}, result)

        result = a & b # letters in both a and b

        self.assertEqual({'a', 'c'}, result)

        result = a ^ b # letters in a or b but not both

        self.assertEqual({'r', 'd', 'b', 'm', 'z', 'l'}, result)