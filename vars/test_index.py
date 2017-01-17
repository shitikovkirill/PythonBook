import unittest

class TestStringMethods(unittest.TestCase):
    def test_prisvaevanie(self):
        a, b = 0, 1
        self.assertTrue(a == 0)
        self.assertTrue(b == 1)

if __name__ == '__main__':
    unittest.main()