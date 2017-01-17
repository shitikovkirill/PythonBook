import unittest

class TestStringMethods(unittest.TestCase):

    def test_base(self):
        print 'string \'"'  # 1 = 2
        print "string '\""
        print '''string'''  # 3 = 4
        print """string"""

        a = '''this
        is ' "
        string'''

        print a

        a = 'string' ' test'
        self.assertTrue(a, 'string test')

        a = 'string' + ' test'
        self.assertTrue(a == 'string test')

    def test_strin_as_array(self):
        print '-------------'
        a = 'string test'
        self.assertEqual(a[0], 's')
        # error a[0]='h'
        print a[0:3]
        print a[3:]
        print a[:4]
        print a[-1]
        print a[-33:300]
        print a[300:-33]

        print '-------------'
        print len(a)

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
        self.assertEqual('Python', str);


if __name__ == '__main__':
    unittest.main()









