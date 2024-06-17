from algorithms.datastructures.linked_list import LinkedList, LinkedListNode


class ChainedHashTable:
    def __init__(self, size: int) -> None:
        self.table = [LinkedList() for _ in range(size)]
        self.size = size

    def _get_linked_list(self, key: int) -> LinkedList:
        return self.table[self.hash(key)]

    def hash(self, key: int) -> int:
        return key % self.size

    def search(self, key: int) -> LinkedListNode | None:
        return self._get_linked_list(key).search(key)

    def insert(self, x: LinkedListNode) -> None:
        self._get_linked_list(x.key).prepend(x)

    def delete(self, x: LinkedListNode) -> None:
        self._get_linked_list(x.key).delete(x)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.table})"
