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
        self.assertEqual('t', a[1])
        self.assertEqual('t', a[10])
        self.assertEqual('t', a[-1])
        with self.assertRaises(TypeError):
            a[0] = 'h'
        with self.assertRaises(IndexError):
            a[100]

        # slice
        self.assertEqual('string test', a[:])
        self.assertEqual('ring test', a[2:])
        self.assertEqual('stri', a[:4])
        self.assertEqual('str', a[0:3])
        self.assertEqual('srn', a[0:6:2])
        self.assertEqual('srn et', a[::2])
        self.assertEqual('tset gnirts', a[::-1])

        self.assertEqual('string test', a[-33:300])
        self.assertEqual('', a[300:-33])
        self.assertEqual(11, len(a))

    def test_multiplication(self):
        str = 'Na' * 4
        self.assertEqual('NaNaNaNa', str)

        str = 3 * 'un' + 'ium'
        self.assertEqual('unununium', str)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_addition(self):
        prefix = 'Py'
        str = prefix + 'thon'
        # prefix 'thon' error
        self.assertEqual('Python', str)

    def test_join(self):
        str_list = ['Hello', 'word']
        self.assertEqual('Hello - word', ' - '.join(str_list))

if __name__ == '__main__':
    unittest.main()