from dataclasses import dataclass, field

from source.datastructures.linked_list import LinkedList, LinkedListNode


@dataclass(slots=True)
class ChainedHashTable:
    size: int = field(repr=False)
    table: list[LinkedList] = field(init=False)

    def __post_init__(self) -> None:
        self.table = [LinkedList() for _ in range(self.size)]

    def _get_linked_list(self, key: int) -> LinkedList:
        """Helper method."""
        return self.table[self._hash(key)]

    def _hash(self, key: int) -> int:
        """Helper method."""
        return key % self.size

    def chained_hash_search(self, key: int) -> LinkedListNode | None:
        """Runtime: O(n). Amortized: O(1)."""
        return self._get_linked_list(key).list_search(key)

    def chained_hash_insert(self, x: LinkedListNode) -> None:
        """Runtime: O(1)."""
        self._get_linked_list(x.key).list_prepend(x)

    def chained_hash_delete(self, x: LinkedListNode) -> None:
        """Runtime: O(1)."""
        self._get_linked_list(x.key).list_delete(x)
