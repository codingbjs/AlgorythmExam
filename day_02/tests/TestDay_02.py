import random
import unittest

from day_02.factorial import factorial


class TestBasic(unittest.TestCase):
    def test_factorial(self):
        n = round(random.randrange(1, 20))
        print(f"{n}! = {factorial(n)}")


if __name__ == '__main__':
    unittest.main()
