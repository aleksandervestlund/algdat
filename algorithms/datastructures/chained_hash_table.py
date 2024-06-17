from algorithms.datastructures.linked_list import LinkedList, LinkedListNode


class ChainedHashTable:
    def __init__(self, size: int) -> None:
        self.table = [LinkedList() for _ in range(size)]
        self.size = size

    def _get_linked_list(self, key: int) -> LinkedList:
        return self.table[self._hash(key)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def chained_hash_search(self, key: int) -> LinkedListNode | None:
        return self._get_linked_list(key).list_search(key)

    def chained_hash_insert(self, x: LinkedListNode) -> None:
        self._get_linked_list(x.key).list_prepend(x)

    def chained_hash_delete(self, x: LinkedListNode) -> None:
        self._get_linked_list(x.key).list_delete(x)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.table})"
