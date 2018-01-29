import unittest


def factorial(number):
    def factorial_gen():
        yield 1
        current_number = 1
        next_number = 2
        while True:
            current_number *= next_number
            yield current_number
            next_number += 1

    fg = factorial_gen()
    while number:
        result = next(fg)
        number -= 1
    return result


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


class TestGenerators(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)

    def test_my_rang(self):
        print(type(my_range))
        print(type(my_range(1, 6)))
        ranger = my_range(1, 8)
        for x in ranger:
            print(x)


if __name__ == '__main__':
    unittest.main()
