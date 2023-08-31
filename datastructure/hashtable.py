class Node:
    def __init__(self, key: str, data):
        self.key = key
        self.data = data
        self.next = None

    def __hash__(self):
        return 31 * sum([ord(s) for s in self.key])

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return f'[key = {self.key} : data = {self.data}]'


class DuplicatedKey(RuntimeError):
    pass


class HashTable:
    def __init__(self, length=30):
        self.max_len = length
        self.table = [None for _ in range(self.max_len)]
        self.length = 0

    def hash(self, node):
        return hash(node) % self.max_len

    def __str__(self):
        res = "[ "

        for link in self.table:
            if link is None:
                continue

            while True:
                res += str(link)
                if link.next is None:
                    break
                link = link.next

        return res + " ]"

    # 키를 해싱해서 데이타를 저장
    # 데이타를 새로 등록 - 중복키가 있으면 저장할 수 없음
    def add(self, key: str, data):
        self.__add_data(key, data, self.__add)
        # 파이썬의 함수는 1급 객체 : 함수형 프로그래밍
        # 1급 객체 : 값으로 넘길 수 있다.
        # 매개변수로 사용할 수 있고, 변수에 담을 수 있고, return 값으로 쓸 수 있다.

    # 키를 해싱해서 데이타를 저장
    # 데이타를 덮어씀
    def set(self, key: str, data):
        self.__add_data(key, data, self.__set)

    def __add(self, link, node):
        if link == node:
            raise DuplicatedKey

    def __set(self, link, node):
        if link == node:
            link.data = node.data
            raise DuplicatedKey

    def __add_data(self, key: str, data, fn):
        if type(key) is not str:
            raise TypeError('문자열 key 만 입력 가능 합니다.')

        node = Node(key, data)
        index = self.hash(node)

        if self.table[index] is None:
            self.table[index] = node
        else:
            link = self.table[index]  # 해당 인덱스에 저장된 첫번째 Node

            while True:
                try:
                    fn(link, node)
                except DuplicatedKey:
                    return

                if link.next is None:
                    link.next = node
                    break

                link = link.next

        self.length += 1

    def get(self, key: str):
        if type(key) is not str:
            raise TypeError('문자열 key 만 입력 가능 합니다.')

        index = self.hash(Node(key, -1))
        link = self.table[index]

        if link is None:  # 미리 리턴할 것인가 루프를 확인하고 리턴할 것인가 개인취향... ...
            return None

        while link is not None:
            if link.key == key:
                return link.data
            link = link.next

        return None

    def __contains__(self, key):
        return True if self.get(key) is not None else False

    def __iter__(self):
        return HashTable.Iterator(self.table)

    class Iterator:
        def __init__(self, hashtable):
            self.hashtable = hashtable
            self.length = len(hashtable) - 1
            self.pointer = 0
            self.link = None

        def __iter__(self):
            return self

        def __next__(self):
            if self.pointer == self.length:
                raise StopIteration

            index = self.hashtable[self.pointer]

            # index 하위에 next 가 있으면 데이타 반환
            if self.link is not None:
                data = index.link.data
                self.link = index.link.next
                return data

            while index is None:
                print(f"index is None : {self.pointer}")
                if self.length == self.pointer:
                    raise StopIteration
                self.pointer += 1
                index = self.hashtable[self.pointer]

            data = index.data
            if index.next is None:
                self.pointer += 1

            self.link = index.next

            return data
