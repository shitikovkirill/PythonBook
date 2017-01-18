from __future__ import absolute_import
import unittest

class TestLambdaMethods(unittest.TestCase):
    def test_lambda(self):
        def make_incrementor(n):
            return lambda x: x + n

        f = make_incrementor(42)
        self.assertEqual(42, f(0));
        self.assertEqual(43, f(1));
