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

