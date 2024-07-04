from __future__ import annotations

from dataclasses import dataclass, field


def list_insert(x: LinkedListNode, y: LinkedListNode) -> None:
    x.next = y.next
    x.prev = y

    if y.next is not None:
        y.next.prev = x

    y.next = x


@dataclass(slots=True)
class LinkedListNode:
    key: int
    prev: LinkedListNode | None = field(default=None, repr=False)
    next: LinkedListNode | None = field(default=None, repr=False)


@dataclass(slots=True, repr=False)
class LinkedList:
    head: LinkedListNode | None = None

    def list_search(self, key: int) -> LinkedListNode | None:
        """O(n)."""
        x = self.head
        while x is not None and x.key != key:
            x = x.next

        return x

    def list_prepend(self, x: LinkedListNode) -> None:
        """O(1)."""
        x.next = self.head
        x.prev = None

        if self.head is not None:
            self.head.prev = x

        self.head = x

    def list_delete(self, x: LinkedListNode) -> None:
        """O(1)."""
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next

        if x.next is not None:
            x.next.prev = x.prev

        del x  # Not part of the original pseudocode.

    def __repr__(self) -> str:
        x = self.head
        keys: list[int] = []

        while x is not None:
            keys.append(x.key)
            x = x.next

        return f"{self.__class__.__name__}({keys})"
