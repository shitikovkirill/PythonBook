from __future__ import absolute_import
import unittest

class TestDictionariesMethods(unittest.TestCase):
    def test_creation(self):
        tel = {'jack': 4098, 'sape': 4139}
        tel['guido'] = 4127

        self.assertIn('guido', tel)
        self.assertEqual(4098, tel['jack'])

        del tel['sape']

        self.assertNotIn('sape', tel)

        result = list(tel.keys())

        self.assertEqual(['jack', 'guido'], result)

        self.assertTrue('guido' in tel)
        self.assertFalse('jack' not in tel)

    def test_create(self):
        result = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

        self.assertEqual({'sape': 4139, 'jack': 4098, 'guido': 4127}, result)

        result = {x: x ** 2 for x in (2, 4, 6)}

        self.assertEqual({2: 4, 4: 16, 6: 36}, result)

        result = dict(sape=4139, guido=4127, jack=4098)

        self.assertEqual({'sape': 4139, 'jack': 4098, 'guido': 4127}, result)

    def test_create2(self):
        lot = [['a', 'b'], ['c', 'd'], ['e', 'f']]

        self.assertEqual({'a': 'b', 'c': 'd', 'e': 'f'}, dict(lot))

    def test_create3(self):
        lot = {'a': 'luz', 'b': 'hbn', 'r': 'nvz', 'a': 'aaa'}
        self.assertEqual({'a': 'aaa', 'b': 'hbn', 'r': 'nvz'}, lot)

    def test_update(self):
        pythons = {'a': 'rr', 'b': 'gg'}
        others = {'g': 'hh'}
        pythons.update(others)
        self.assertEqual({'a': 'rr', 'b': 'gg', 'g': 'hh'}, pythons)

        others2 = {'g': 'hh', 'b': 'hh'}
        pythons.update(others2)
        self.assertEqual({'a': 'rr', 'b': 'hh', 'g': 'hh'}, pythons)

    def test_clear(self):
        pythons = {'a': 'rr', 'b': 'gg'}
        pythons.clear()
        self.assertEqual({}, pythons)

    def test_get(self):
        pythons = {'a': 'rr', 'b': 'gg'}
        self.assertEqual('rr', pythons['a'])

        with self.assertRaises(KeyError):
            pythons['d']

        self.assertFalse('d' in pythons)

    def test_get(self):
        pythons = {'a': 'rr', 'b': 'gg'}

        self.assertEqual('rr', pythons.get('a'))
        self.assertEqual('yra!!', pythons.get('t', 'yra!!'))
        self.assertEqual(None, pythons.get('t'))


if __name__ == '__main__':
    unittest.main()