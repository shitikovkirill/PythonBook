import unittest


class TestStrings(unittest.TestCase):
    def test_multi_line_string(self):
        str1 = "test " + \
            "test"
        self.assertEqual('test test', str1)

        str1 = ("test "
                "test")
        self.assertEqual('test test', str1)

    def test_unicod(self):
        # for 3 python
        self.assertEqual('€', '\N{euro sign}')
        self.assertEqual('€', '\u20AC')

    def test_ord(self):
        self.assertEqual(8364, ord('€'))

    def test_chr(self):
        self.assertEqual('€', chr(8364))

    def test_ascii(self):
        self.assertEqual("'\\u20ac'", ascii('€'))


if __name__ == '__main__':
    unittest.main()