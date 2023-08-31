import random
import unittest

from datastructure.list_q import check_max, check_max2, check_palindrome, check_palindrome2


class TestListQ(unittest.TestCase):
    def test_check_max(self):
        arr = [round(random.randrange(1, 1000)) for _ in range(1000)]
        answer = check_max(arr)
        expect = max(arr)
        print(f"check_max : {answer}, max : {expect}")
        self.assertEquals(answer, expect)

    def test_check_max2(self):
        arr = [round(random.randrange(1, 1000)) for _ in range(1000)]
        answer = check_max2(arr)
        arr.sort(reverse=True)
        expect = arr[:2]
        print(f"check_max : {answer}, max : {expect}")
        self.assertEquals(answer, expect)

    def test_palindrome(self):
        texts = ['tomato', '토마토', '기러기', 'Wild goose', '역삼역', 'Yeoksam station']
        for text in texts:
            if check_palindrome2(text):
                print(text + ' 는 회문입니다.')


if __name__ == '__main__':
    unittest.main()
