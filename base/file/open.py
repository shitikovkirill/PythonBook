import unittest
from os.path import isfile


class TestFile(unittest.TestCase):

    def test_create_file(self):
        file = open("/home/kirill/Programming/Python/Book/base/file/dell_this.txt", "w")
        file.write("First line\n")
        file.write("Second line")
        file.close()
        self.assertTrue(isfile('/home/kirill/Programming/Python/Book/base/file/dell_this.txt'))

    def test_rewrite(self):
        file = open("/home/kirill/Programming/Python/Book/base/file/rewrite.txt", "r+")
        lines = []
        for line in file:
            lines.append(line)
        file.seek(0)
        file.write("First line\n")
        file.write("Second line")
        file.truncate()
        file.close()
        self.assertTrue("First line\n" in lines)
        self.assertTrue("Second line" in lines)

if __name__ == '__main__':
    unittest.main()
