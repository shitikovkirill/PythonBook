from __future__ import absolute_import
import unittest

class TestListMethods(unittest.TestCase):

    def test_append(self):
        list = [24,58,234,89,34]

        list.append('item')

        self.assertEqual(6, len(list))
        self.assertEqual('item', list[5])

        list[len(list):] = ['item2']

        self.assertEqual(7, len(list))
        self.assertEqual('item2', list[6])

    def test_extend(self):
        list = [24, 58, 234, 89, 34]
        list2 = ['item', 'item2']

        list.extend(list2)
        self.assertEqual([24, 58, 234, 89, 34, 'item', 'item2'], list)

        list = [24, 58, 234, 89, 34]
        list2 = ['item', 'item2']

        list[len(list):] = list2
        self.assertEqual([24, 58, 234, 89, 34, 'item', 'item2'], list)