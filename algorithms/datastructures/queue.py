from typing import Any


class Queue:
    def __init__(self, size: int) -> None:
        self.queue: list[Any] = []
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, x: Any) -> None:
        self.queue[self.tail] = x
        if self.tail == self.size:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> Any:
        x = self.queue[self.head]
        if self.head == self.size:
            self.head = 0
        else:
            self.head += 1
        return x
