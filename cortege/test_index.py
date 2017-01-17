import unittest

class TestStringMethods(unittest.TestCase):
    def test_criation(self):
        t = 12345, 54321, 'hello!'
        self.assertEqual(12345, t[0])

        t2 = (1, 5, 'hello2!')

        u = t , t2
        self.assertEqual(((12345, 54321, 'hello!'),(1, 5, 'hello2!')), u)

        empty = ()
        print empty
        a =(22,)
        print a

    def test_rasspakovka(self):
        t = 12345, 54321, 'hello!'
        a,b,c = t

        self.assertEqual(12345, a)
        self.assertEqual(54321, b)
        self.assertEqual('hello!', c)



