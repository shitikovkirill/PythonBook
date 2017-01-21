import unittest

class TestStringMethods(unittest.TestCase):

    def test_base(self):

        a = 'string' ' test'
        self.assertTrue(a, 'string test')

        a = 'string' + ' test'
        self.assertTrue(a == 'string test')

    def test_strin_as_array(self):
        a = 'string test'
        self.assertEqual('s', a[0])
        # error a[0]='h'

        self.assertEqual('str', a[0:3])
        self.assertEqual('ing test', a[3:])
        self.assertEqual('stri', a[:4])
        self.assertEqual('t', a[-1])
        self.assertEqual('string test', a[-33:300])
        self.assertEqual('', a[300:-33])
        self.assertEqual(11, len(a))

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_multiplication(self):
        str = 3 * 'un' + 'ium'
        self.assertEqual('unununium', str)

    def test_addition(self):
        prefix = 'Py'
        str = prefix + 'thon'
        # prefix 'thon' error
        self.assertEqual('Python', str)