import random
import unittest

from brute_force.bubble_sort import *
from brute_force.selection_sort import *


class TestSort(unittest.TestCase):
    def test_bibble_sort(self):
        arr = [round(random.randrange(1, 1000)) for _ in range(1000)]
        print(selection_sort(arr))
        # print(bubble_sort3(arr))


if __name__ == '__main__':
    unittest.main()
