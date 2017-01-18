from __future__ import absolute_import
import unittest

class TestCortegeMethods(unittest.TestCase):
    def test_criation(self):
        t = 12345, 54321, 'hello!'
        self.assertEqual(12345, t[0])

        t2 = (1, 5, 'hello2!')

        u = t , t2
        self.assertEqual(((12345, 54321, 'hello!'),(1, 5, 'hello2!')), u)

        empty = ()
        self.assertEqual(0, len(empty))

        empty =(22,)
        self.assertEqual(1, len(empty))
        self.assertEqual(22, empty[0])

    def test_rasspakovka(self):
        t = 12345, 54321, 'hello!'
        a,b,c = t

        self.assertEqual(12345, a)
        self.assertEqual(54321, b)
        self.assertEqual('hello!', c)



