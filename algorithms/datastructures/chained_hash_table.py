from algorithms.datastructures.linked_list import LinkedList
from algorithms.datastructures.node import Node


class ChainedHashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]

    def hash(self, x: Node) -> int:
        return x.key % self.size

    def insert(self, x: Node) -> None:
        self.table[self.hash(x)].prepend(x)

    def __repr__(self) -> str:
        return f"ChainedHashTable({self.table})"
