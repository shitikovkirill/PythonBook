import unittest

class TestCopyMethods(unittest.TestCase):

    def test_without_copy(self):
        list = [1, 2, 3]
        b = list
        list[0] = 'str'
        self.assertEqual(['str', 2, 3], b)

    def test_copy(self):
        list = [1, 2, 3]

        b = list.copy()

        list[0] = 'str'
        self.assertEqual(['str', 2, 3], list)
        self.assertEqual([1, 2, 3], b)

    def test_list(self):
        arr_list = [1, 2, 3]

        b = list(arr_list)

        arr_list[0] = 'str'
        self.assertEqual(['str', 2, 3], arr_list)
        self.assertEqual([1, 2, 3], b)

    def test_diapazon(self):
        arr_list = [1, 2, 3]

        b = arr_list[:]

        arr_list[0] = 'str'
        self.assertEqual(['str', 2, 3], arr_list)
        self.assertEqual([1, 2, 3], b)

if __name__ == '__main__':
    unittest.main()