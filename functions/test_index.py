from __future__ import absolute_import
import unittest

class TestFunctionMethods(unittest.TestCase):
    def test_unpacking(self):
        args = [3, 6]
        range_var = range(*args)
        self.assertEqual([3, 4, 5], range_var)

        def parrot(voltage, state='a stiff', action='voom'):
            self.assertEqual('four million', voltage)
            self.assertEqual("bleedin' demised", state)
            self.assertEqual("VOOM", action)

        d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
        parrot(**d)
