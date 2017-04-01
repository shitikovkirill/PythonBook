import unittest

class TestDiapasonMethods(unittest.TestCase):

    def test_index(self):
        arr = ['a', 'b', 'c']
        self.assertEqual(['a', 'b'], arr[0:2])

        self.assertEqual(['a', 'c'], arr[::2])

        self.assertEqual(['c', 'a'], arr[::-2])


if __name__ == '__main__':
    unittest.main()