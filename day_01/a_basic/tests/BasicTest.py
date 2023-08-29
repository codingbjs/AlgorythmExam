import unittest

from day_01.a_basic.c_math import *


class TestBasic(unittest.TestCase):
    def test_is_prime(self):
        print(is_prime(2))
        # is_prime_2(3)
        # su_num(10)

    def test_is_prime_list(self):
        print(is_prime_list(10))


if __name__ == '__main__':
    unittest.main()
