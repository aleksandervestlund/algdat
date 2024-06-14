from typing import Any

from algorithms.datastructures.node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def search(self, key: Any) -> Node | None:
        x = self.head
        while x is not None and x.key != key:
            x = x.next
        return x

    def prepend(self, x: Node) -> None:
        x.next = self.head
        x.prev = None
        if self.head is not None:
            self.head.prev = x
        self.head = x

    def insert(self, x: Node, y: Node) -> None:
        x.next = y.next
        x.prev = y
        if y.next is not None:
            y.next.prev = x
        y.next = x

    def delete(self, x: Node) -> None:
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
        return f"LinkedList({keys})"
