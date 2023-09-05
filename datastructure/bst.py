class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.data


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return

        link = self.root

        while True:
            if data <= link.data:
                if link.left_child is None:
                    link.left_child = node
                    break
                link = link.left_child
            else:
                if link.right_child is None:
                    link.right_child = node
                    break
                link = link.right_child

    def find(self, data):
        link = self.root

        while True:
            if link is None:
                return False
            elif data == link.data:
                return True
            elif data < link.data:
                link = link.left_child
            else:
                link = link.right_child

    # 깊이 우선 탐색
    def dfs(self, _type):
        type_dict = {
            'inorder': self.__in_order(self.root),
            'preorder': self.__pre_order(self.root),
            'postorder': self.__post_order(self.root),
        }
        return type_dict.get(_type)

    def __in_order(self, link):
        res = []

        if link.left_child is not None:
            res += self.__in_order(link.left_child)

        if link is not None:
            res += [link.data]

        if link.right_child is not None:
            res += self.__in_order(link.right_child)

        return res

    def __pre_order(self, link):
        res = []

        if link is not None:
            res += [link.data]

        if link.left_child is not None:
            res += self.__pre_order(link.left_child)

        if link.right_child is not None:
            res += self.__pre_order(link.right_child)

        return res

    def __post_order(self, link):
        res = []

        if link.left_child is not None:
            res += self.__post_order(link.left_child)

        if link.right_child is not None:
            res += self.__post_order(link.right_child)

        if link is not None:
            res += [link.data]

        return res
