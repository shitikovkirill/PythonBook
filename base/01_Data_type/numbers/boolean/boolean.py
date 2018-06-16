from __future__ import absolute_import
import unittest


class TestBooleanMethods(unittest.TestCase):

    def test_is_false(self):
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse('')
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse(())
        self.assertFalse(set())

    def test_boolean(self):
        x = 6
        self.assertTrue(5 < x < 10)



if __name__ == '__main__':
    unittest.main()