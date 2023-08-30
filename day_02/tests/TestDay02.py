import random
import unittest

from day_02.fibonacci import fibonacci


class TestDay02(unittest.TestCase):
    # def test_factorial(self):
    #     n = round(random.randrange(1, 20))
    #     print(f"{n}! = {factorial(n)}")

    def test_fibonacci(self):
        n = round(random.randrange(1, 20))
        print(f"{n} fibonacci = {fibonacci(n)}")


if __name__ == '__main__':
    unittest.main()
