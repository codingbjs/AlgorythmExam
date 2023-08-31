class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드의 주소를 저장


# __메서드__ (매직메서드, 던더메서드) 파이썬에서 제공하는 내장 메서드
# 덕타이핑 : 객체의 속성 및 메서드의 집합이 객체의 타입을 결정하는 것

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        node = self.head
        if node is None:
            return '비어있습니다.'
        res = "["
        while node.link:
            res += str(node.data) + ", "
            node = node.link
        res += str(node.data) + "]"
        return res

    def __len__(self):
        return self.length

    # 리스트에 데이타 추가
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            prev = self.head
            # prev.next == None 일때 까지 탐색
            while prev.next:
                prev = prev.next
            # prev.next == None 인 next 에 추가 하는 node 를 저장
            prev.next = node
        self.length += 1

    # 리스트에 첫번째 데이타를 추가
    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            # self.head, node.next = node, self.head
            node.next = self.head
            self.head = node
        self.length += 1

    def insert(self, i, data):
        if i < 0:
            raise IndexError("인덱스는 0보다 커야합니다.")
        if i == 0:
            self.prepend(data)
            return
        if i >= self.length:
            self.append(data)
            return

        node = Node(data)
        prev = self.head

        for _ in range(i - 1):
            prev = prev.next

        node.next = prev.next
        prev.next = node
        self.length += 1

    def pop(self):
        node = self.head
        # node 가 없는 경우
        if node is None:
            return None

        # node 가 1개 있는 경우
        if node.link is None:
            self.head = None
            self.length -= 1
            return node.data

        # 노드가 1개 이상인 경우 마지막 데이타를 반환하고 삭제함.
        prev = node
        while node.link:
            prev = node
            node = node.link

        prev.link = None
        self.length -= 1
        return node.data

    # 첫번째 데이타를 반환하고 삭제함.
    def popleft(self):
        node = self.head
        if node is None:
            return None
        self.head = self.head.link
        self.length -= 1
        return node.data

    # 매개변수로 받은 data 와 같은 첫번째 data 를 삭제하고 성공여부 Bool 반환
    def remove(self, data):
        node = self.head
        if node.data == data:
            self.popleft()
            return True

        while node.link:
            if node.link.data == data:
                node.link = node.link.link
                self.length -= 1
                return True
            node = node.link

        return False

    # 역순 정렬
    def reverse(self):
        if self.length <= 1:
            return

        prev = None
        node = self.head
        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
        self.head = prev

    def __iter__(self):
        return LinkedList.Iterator(self.head)

    class Iterator:
        def __init__(self, node):
            self.node = node
            self.call_cnt = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.node is None:
                raise StopIteration
            print(f"{self.call_cnt}번째 호출입니다.{self.node.data}")
            data = self.node.data
            self.node = self.node.link
            self.call_cnt += 1
            return data


if __name__ == '__main__':
    _list = LinkedList()
    print(_list)
