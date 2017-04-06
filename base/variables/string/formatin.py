import unittest

class TestStringMethods(unittest.TestCase):

    def test_format(self):
        self.assertEqual('one - two', '%s - %s' % ('one', 'two')) #old
        self.assertEqual('one - two', '{} - {}'.format('one', 'two'))


if __name__ == '__main__':
    unittest.main()