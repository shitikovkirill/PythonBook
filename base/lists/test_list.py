from __future__ import absolute_import
import unittest

class TestListMethods(unittest.TestCase):

    def test_append(self):
        list = [24, 58, 234, 89, 34]

        list.append('item')

        self.assertEqual(6, len(list))
        self.assertEqual('item', list[5])

        list[len(list):] = ['item2']

        self.assertEqual(7, len(list))
        self.assertEqual('item2', list[6])

    def test_extend(self):
        # 1
        list = [24, 58, 234, 89, 34]
        list2 = ['item', 'item2']

        list.extend(list2)
        self.assertEqual([24, 58, 234, 89, 34, 'item', 'item2'], list)

        # 2
        list = [24, 58, 234, 89, 34]
        list2 = ['item', 'item2']

        list[len(list):] = list2
        self.assertEqual([24, 58, 234, 89, 34, 'item', 'item2'], list)

        # 3
        list = [24, 58, 234, 89, 34]
        list2 = ['item', 'item2']
        list += list2
        self.assertEqual([24, 58, 234, 89, 34, 'item', 'item2'], list)

    def test_insert(self):
        list = [24, 58, 234, 89, 34]
        list.insert(0, 'test')

        self.assertEqual('test', list[0])

        list.insert(4, 'test2')
        self.assertEqual('test2', list[4])

        list.insert(4000, 'test3')
        self.assertEqual('test3', list[-1])

    def test_remove(self):
        list = [24, 58, 234, 89, 34]

        list.remove(24);
        self.assertEqual(58, list[0])

        with self.assertRaises(ValueError):
            list.remove(0);

    def test_pop(self):
        list = [24, 58, 234, 89, 34]

        item = list.pop()

        self.assertEqual(4, len(list))
        self.assertEqual(89, list[len(list)-1])
        self.assertEqual(34, item)

        list = [24, 58, 234, 89, 34]

        item = list.pop(1)

        self.assertEqual(4, len(list))
        self.assertEqual(234, list[1])
        self.assertEqual(58, item)

    def test_index(self):
        list = [24, 58, 234, 89, 34, 24]

        index = list.index(24)

        self.assertEqual(0, index)

        index = list.index(24, 1)

        self.assertEqual(5, index)

        with self.assertRaises(ValueError):
            index = list.index(24, 1, 3)

    def test_count(self):
        list = [24, 58, 234, 89, 34, 24]

        count = list.count(24)
        self.assertEqual(2, count)

    def test_sort(self):
        list = [24, 58, 234, 89, 34, 24]
        list.sort()

        self.assertEqual([24, 24, 34, 58, 89, 234], list)

    def test_reverse(self):
        list = [24, 58, 234, 89, 34, 24]
        list.reverse()

        self.assertEqual([24, 34, 89, 234, 58, 24], list)

    def test_dell(self):
        list = [24, 58, 234, 89, 34, 24]
        del list[1:]
        self.assertEqual([24], list)

    def test_in(self):
        list = [24, 58, 234, 89, 34, 24]
        self.assertTrue(24 in list)

if __name__ == '__main__':
    unittest.main()