import unittest

class TestDictionariesMethods(unittest.TestCase):

    def test_key(self):
        dictionaries = {'a': 23, 'b': 45, 'c': 76, }
        get_keys = dictionaries.keys()
        key_list = list(get_keys)

        self.assertTrue(
            'b' in key_list and
            'c' in key_list and
            'a' in key_list)

    def test_values(self):
        dictionaries = {'a': 23, 'b': 45, 'c': 76}
        get_values = dictionaries.values()
        values_list = list(get_values)

        self.assertTrue(
            23 in values_list and
            45 in values_list and
            76 in values_list)


    def test_items(self):
        dictionaries = {'a': 23, 'b': 45, 'c': 76}
        items = list(dictionaries.items())

        self.assertTrue(
            ('a', 23) in items and
            ('b', 45) in items and
            ('c', 76) in items)

    def test_copy(self):
        dictionaries = {'a': 23, 'b': 45, 'c': 76}
        new_dictionaries = dictionaries.copy()
        self.assertTrue(dictionaries == new_dictionaries)


if __name__ == '__main__':
    unittest.main()