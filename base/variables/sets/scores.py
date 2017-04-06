import unittest

class TestDictionariesMethods(unittest.TestCase):

    def test_index(self):
        empty_set = set()
        print(empty_set)

    def test_set(self):
        v = set('letters')
        self.assertTrue('t' in v)

    def test_action_intersection(self):
        a = {1, 2}
        b = {2, 3}
        c = a & b
        c2 = a.intersection(b)

        self.assertTrue(c == c2)

    def test_action_union(self):
        a = {1, 2}
        b = {2, 3}
        c = a | b
        c2 = a.union(b)
        self.assertTrue(c == c2)

    def test_action_difference(self):
        a = {1, 2}
        b = {2, 3}

        c = a - b
        c2 = a.difference(b)

        self.assertTrue(c == c2)
        self.assertEqual({1}, c)

        d = b - a
        d2 = b.difference(a)

        self.assertTrue(d == d2)
        self.assertEqual({3}, d)

    def test_symmetric_difference(self):
        a = {1, 2}
        b = {2, 3}

        c = a ^ b
        c2 = a.symmetric_difference(b)

        self.assertTrue(c == c2)
        self.assertEqual({1, 3}, c)

    def test_(self):
        a = {1, 2}
        b = {2, 3}

        c = a <= b
        c2 = a.issubset(b)

        self.assertFalse(c)
        self.assertFalse(c2)

if __name__ == '__main__':
    unittest.main()