import unittest

from datastructure.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)

        print(stack)

    def test_pop(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)

        for i in range(10):
            print(stack.pop(), end='')

    def test_pick(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)

        for i in range(10):
            print(stack.peek(), end='')

        print(f' : 스택이 비었습니까? : {stack.is_empty()}')

        for i in range(10):
            print(stack.pop(), end='')

        print(f' : 스택이 비었습니까? : {stack.is_empty()}')


if __name__ == '__main__':
    unittest.main()