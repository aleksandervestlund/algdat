from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LinkedListNode:
    key: int
    prev: LinkedListNode | None = None
    next: LinkedListNode | None = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.key})"


class LinkedList:
    def __init__(self) -> None:
        self.head: LinkedListNode | None = None

    def search(self, key: int) -> LinkedListNode | None:
        x = self.head
        while x is not None and x.key != key:
            x = x.next

        return x

    def prepend(self, x: LinkedListNode) -> None:
        x.next = self.head
        x.prev = None

        if self.head is not None:
            self.head.prev = x

        self.head = x

    @staticmethod
    def insert(x: LinkedListNode, y: LinkedListNode) -> None:
        x.next = y.next
        x.prev = y

        if y.next is not None:
            y.next.prev = x

        y.next = x

    def delete(self, x: LinkedListNode) -> None:
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next

        if x.next is not None:
            x.next.prev = x.prev
        # del x

    def __repr__(self) -> str:
        x = self.head
        keys = []

        while x is not None:
            keys.append(x.key)
            x = x.next

        return f"{self.__class__.__name__}({keys})"
