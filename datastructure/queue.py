class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.front is None:
            return '비어있는 큐입니다.'
        node = self.front
        res = "[ front << "
        while node.next is not None:
            res += str(node.data) + " , "
            node = node.next

        return res + str(node.data) + " << rear ]"

    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.length += 1

    def dequeue(self):
        node = self.front
        if node is None:
            return None

        if node == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

        self.length -= 1
        return node.data

    def is_empty(self):
        return self.front is None
