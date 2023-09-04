import unittest


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        from datastructure.queue import Queue
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)

            # ----여기부터
        for i in range(10):
            print(queue.dequeue(), end='')

        print()
        # ------ 여기 지우면 큐가 들어감
        print(queue)


if __name__ == '__main__':
    unittest.main()
