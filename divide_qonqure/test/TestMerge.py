import random
import unittest

from divide_qonqure.merge_sort import merge


class TestMerge(unittest.TestCase):
    def test_merge(self):
        arr1 = [round(random.randrange(1, 1000)) for _ in range(300)]
        arr2 = [round(random.randrange(1, 1000)) for _ in range(300)]
        arr1.sort()
        arr2.sort()
        print(merge(arr1, arr2))


if __name__ == '__main__':
    unittest.main()
