import unittest

from datastructure.bst import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def test_insert(self):
        arr = [10, 1002, 345, 11, 7545, 44, 12612, 232]
        bst = BinarySearchTree()
        for i in arr:
            bst.insert(i)

        print(bst.dfs('inorder'))

    def test_dfs(self):
        bst = BinarySearchTree()
        for i in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            bst.insert(i)

        print(bst.dfs('inorder'))
        print(bst.dfs('preorder'))  # 전위순회하여 결과를 반환
        print(bst.dfs('postorder'))  # 후위순회하여 결과를 반환
        print(bst.find(6))
        print(bst.find(15))
        bst.bfs()


if __name__ == '__main__':
    unittest.main()
