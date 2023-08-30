import random
import unittest

from day_01.c_math import *


class TestBasic(unittest.TestCase):
    # def test_is_prime(self):
    #     # self.assertTrue(is_prime(2))
    #     pass

    # def test_is_prime_list(self):
    #     # print(is_prime_list(10))
    #     pass

    # def test_gcd1(self):
    #     left = round(random.randrange(1, 1000))
    #     right = round(random.randrange(1, 1000))
    #     print(f"left  :{left} , right : {right}")
    #     print(f"gcd({gcd(left, right)}) == gcd1({gcd1(left, right)}) ")
    #     self.assertTrue(gcd(left, right) == gcd1(left, right))

    # def test_gcd2(self):
    #     left = round(random.randrange(1, 1000))
    #     right = round(random.randrange(1, 1000))
    #     print(f"left  :{left} , right : {right}")
    #     print(f"gcd({gcd(left, right)}) == gcd2({gcd2(left, right)}) ")
    #     self.assertTrue(gcd(left, right) == gcd2(left, right))

    # def test_gcd3(self):
    #     left = round(random.randrange(1, 1000))
    #     right = round(random.randrange(1, 1000))
    #     print(f"left  :{left} , right : {right}")
    #     print(f"gcd({gcd(left, right)}) == gcd3({gcd2(left, right)}) ")
    #     self.assertTrue(gcd(left, right) == gcd3(left, right))

    def test_lcm(self):
        left = round(random.randrange(1, 1000))
        right = round(random.randrange(1, 1000))
        print(f"left  :{left} , right : {right}")
        print(f"lcm({lcm(left, right)}) == lcm1({lcm1(left, right)}) ")
        self.assertTrue(lcm(left, right) == lcm1(left, right))




if __name__ == '__main__':
    unittest.main()
