import unittest

from datastructure.hashtable import HashTable


class TestHashTable(unittest.TestCase):
    def test_hash_table(self):
        hash_table = HashTable()
        hash_table.add('a', 100)
        hash_table.add('b', 200)
        hash_table.add('c', 300)
        print(hash_table)
        hash_table.set('a', 500)
        print(hash_table)


if __name__ == '__main__':
    unittest.main()
