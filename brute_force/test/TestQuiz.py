import random
import unittest

from brute_force.brute_force_q import *


class TestQuiz(unittest.TestCase):
    def test_quiz(self):
        n = round(random.randrange(1, 11))
        print(doom_day(n))

    def test_dwarf(self):
        arr = [round(random.randrange(10, 15)) for _ in range(7)]
        t = 100 - sum(arr)
        arr[6] = arr[6] + t

        arr.append(round(random.randrange(1, 20)))
        arr.append(round(random.randrange(1, 20)))
        print(arr)
        print(dwarf(arr))


if __name__ == '__main__':
    unittest.main()
