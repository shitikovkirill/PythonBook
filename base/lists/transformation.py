import unittest

class TestListMethods(unittest.TestCase):

    def test_list(self):
        self.assertEqual(['c', 'a', 't'], list('cat'))
        a_tuple = ('ready', 'fire', 'aim')
        self.assertEqual(['ready', 'fire', 'aim'], list(a_tuple))

    def test_split(self):
        splitme ='a/b//c/d///e'

        self.assertEqual(['a/b', 'c/d', '/e'], splitme.split('//'))

    def test_join(self):
        join_str = "', '".join(['ff', 'tt', 'th'])
        self.assertEqual("ff', 'tt', 'th", join_str)


if __name__ == '__main__':
    unittest.main()