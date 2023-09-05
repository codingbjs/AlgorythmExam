import random
import unittest

from divide_qonqure.merge_sort import *
from divide_qonqure.merge_sort_2 import *
from divide_qonqure.quick_sort import quick_sort


class TestMerge(unittest.TestCase):
    def test_merge(self):
        arr1 = [round(random.randrange(1, 1000)) for _ in range(300)]
        arr2 = [round(random.randrange(1, 1000)) for _ in range(300)]
        arr1.sort()
        arr2.sort()
        print(merge(arr1, arr2))

    def test_merge_sort(self):
        arr1 = [round(random.randrange(1, 1000)) for _ in range(1000)]
        print(merge_sort(arr1))

    def test_merge_sort_2(self):
        arr1 = [round(random.randrange(1, 1000)) for _ in range(1000)]
        merge_sort_2(arr1, 0, len(arr1)-1)
        print(arr1)

    def test_quick_sort(self):
        arr1 = [round(random.randrange(1, 1000)) for _ in range(1000)]
        quick_sort(arr1, 0, len(arr1)-1)
        print(arr1)


if __name__ == '__main__':
    unittest.main()
