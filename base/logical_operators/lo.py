import unittest

class TestLogicalOperators(unittest.TestCase):

    def test_if(self):
        a = 4
        result = 5 < a < 10
        self.assertFalse(result)

        a = 6
        result = 5 < a < 10
        self.assertTrue(result)

    def test_is(self):
        a = ['one', 1, None]
        b = ['one', 1, None]

        self.assertFalse(a is b)

        a = b
        self.assertTrue(a is b)

        c = None
        self.assertTrue(c is None)

        with self.assertRaises(NameError):
            self.assertTrue(d is None)

    def test_is2(self):
        x = [0]
        self.assertFalse(x is None)
        self.assertTrue(not x is None)
        # =
        self.assertTrue(not (x is None))
        # =
        self.assertTrue(x is not None)

        self.assertFalse((not x) is None)

    def test_in(self):
        l = [1, 2, 3]
        self.assertTrue(2 in l)

        str = 'Hello world'
        self.assertTrue('world' in str)

    def test_and(self):
        five = 5
        two = 2
        zero = 0

        self.assertEqual(2, five and two)
        self.assertEqual(5, two and five)

        self.assertEqual(0, five and zero)
        self.assertEqual(0, two and zero)
        self.assertEqual(0, zero and five)
        self.assertEqual(0, zero and two)

    def test_or(self):
        five = 5
        two = 2
        zero = 0
        nothin = 0

        self.assertEqual(5, five or two)
        self.assertEqual(2, two or five)

        self.assertEqual(5, five or zero)
        self.assertEqual(2, two or zero)
        self.assertEqual(5, zero or five)
        self.assertEqual(2, zero or two)

        self.assertEqual(0, zero or nothin)
        self.assertEqual(None, zero or None)
        self.assertEqual(0, None or zero)

    def test_not(self):
        self.assertEqual(True, not False)
        self.assertEqual(True, not 0)

        self.assertEqual(False, not True)
        self.assertEqual(False, not 1)


if __name__ == '__main__':
    unittest.main()