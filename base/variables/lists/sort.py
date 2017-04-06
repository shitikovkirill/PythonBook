import unittest

class TestSortMethods(unittest.TestCase):

    def test_sort(self):
        list = ['f', 'a', 'c']
        list.sort()
        self.assertEqual(['a', 'c', 'f'], list)

        list = ['f', 'a', 'c']
        list.sort(reverse=True)
        self.assertEqual(['f', 'c', 'a'], list)

    def test_sorted(self):
        list = ['f', 'a', 'c']
        new_list = sorted(list)
        self.assertEqual(['f', 'a', 'c'], list)
        self.assertEqual(['a', 'c', 'f'], new_list)


if __name__ == '__main__':
    unittest.main()