from __future__ import absolute_import
import unittest

class TestStringMethods(unittest.TestCase):
    def test_prisvaevanie(self):
        a = ['spam', 'eggs', 100, 1234]
        self.assertEqual('spam', a[0])
        self.assertEqual(100, a[2])
        self.assertEqual(100, a[-2])
        self.assertEqual(['eggs', 100], a[1:-1])
        self.assertEqual(['spam', 'eggs', 100, 1234], a[:])

    def test_deystviya(self):
        a = ['spam', 'eggs', 100, 1234]

        self.assertEqual(['spam', 'eggs', 100, 1234, 'bacon', 4], a+['bacon', 2*2])
        self.assertEqual(['spam', 'eggs', 100, 1234, 'spam', 'eggs', 100, 1234], a*2)
        a[1:3] = [22, 33]
        self.assertEqual(['spam', 22, 33, 1234], a)

        a = [123, 456]
        a[1:1] = ['cccc', 'wwww']
        self.assertEqual([123, 'cccc', 'wwww', 456], a)

    def test_dobavlenie(self):
        a = []

        a += [22]
        self.assertEqual([22], a)

        a.append('cc')
        self.assertEqual([22, 'cc'], a)

        a.extend(['ww', 55])
        self.assertEqual([22, 'cc', 'ww', 55], a)

        a.insert(len(a), 'tt')
        self.assertEqual([22, 'cc', 'ww', 55, 'tt'], a)

    def test_udalenie(self):
        a = [22, 'cc', 'ww', 55, 'tt']
        del a[-1]
        self.assertEqual([22, 'cc', 'ww', 55], a)

        a.remove('cc')
        self.assertEqual([22, 'ww', 55], a)

        a.pop()
        self.assertEqual([22, 'ww'], a)

        b = a.pop(0)
        self.assertEqual(22, b)
        self.assertEqual(['ww'], a)

    def test_change_list(self):
        a = [1, 5, 7, 13, 22]

        b = [elem*2 for elem in a]

        self.assertEqual([2, 10, 14, 26, 44], b)

    def test_tuple_to_list(self):
        t = 'one', 'two', 'three'
        l = list(t)
        self.assertEqual(['one', 'two', 'three'], l)

if __name__ == '__main__':
    unittest.main()
