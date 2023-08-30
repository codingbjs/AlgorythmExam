import unittest

from datastructure.linkedlist import LinkedList


class TestDataStructure(unittest.TestCase):
    def test_linked_list(self):
        _list = LinkedList()
        for i in range(10):
            _list.append(i)
        print(_list)

        _list.prepend(-1)
        print(_list)

        _list.insert(5, 100)
        print(len(_list))

        print(_list.pop())
        print(_list)

        print(_list.popleft())
        print(_list)

        print(_list.remove(100))
        print(_list)

        # for itme in _list:
        #     print(itme)

        _list.reverse()
        print(_list)


if __name__ == '__main__':
    unittest.main()
