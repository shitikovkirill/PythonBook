import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_swapcase(self):
        str = 'Hello word'
        self.assertEqual(str.swapcase(), 'hELLO WORD')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_join(self):
        str_list = ['Hello', 'word']
        self.assertEqual('Hello - word', ' - '.join(str_list))

    def test_str_with(self):
        str = 'Hello word'
        self.assertTrue(str.startswith('He'))
        self.assertTrue(str.endswith('rd'))

    def test_find(self):
        str = 'Hello word'
        self.assertEqual(6, str.find('w'))

        self.assertEqual(2, str.find('l'))
        self.assertEqual(3, str.rfind('l'))

    def test_count(self):
        str = 'Hello word'
        self.assertEqual(2, str.count('l'))

    def test_is_num(self):
        self.assertTrue('12313'.isalnum())
        self.assertFalse('Hello word'.isalnum())

    def test_strip(self):
        str = 'Hello word'
        self.assertEqual('Hello ', str.strip('word'))

    def test_alignment(self):
        str = 'Hello word'
        self.assertEqual('   Hello word  ', str.center(15))
        self.assertEqual('Hello word     ', str.ljust(15))
        self.assertEqual('     Hello word', str.rjust(15))

    def test_replace(self):
        str = 'Hello word word word'
        self.assertEqual('Hello  -   -   - ', str.replace('word', ' - '))
        self.assertEqual('Hello  -   -  word', str.replace('word', ' - ', 2))

if __name__ == '__main__':
    unittest.main()

    # 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find',
    # 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle',
    # 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex',
    # 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
    # 'swapcase', 'title', 'translate', 'upper', 'zfill'
