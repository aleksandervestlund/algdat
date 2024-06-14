from algorithms.datastructures.linked_list import LinkedList
from algorithms.datastructures.node import Node


class ChainedHashTable:
    def __init__(self, size: int):
        self.table = [LinkedList() for _ in range(size)]
        self.size = size

    def _get_linked_list(self, key: int) -> LinkedList:
        return self.table[self.hash(key)]

    def hash(self, key: int) -> int:
        return key % self.size

    def search(self, key: int) -> Node | None:
        return self._get_linked_list(key).search(key)

    def insert(self, x: Node) -> None:
        self._get_linked_list(x.key).prepend(x)

    def delete(self, x: Node) -> None:
        self._get_linked_list(x.key).delete(x)

    def __repr__(self) -> str:
        return f"ChainedHashTable({self.table})"
