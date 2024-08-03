from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Queue:
    """FIFO (First in, first out) data structure."""

    size: int = field(repr=False)
    queue: list[Any] = field(init=False)
    head: int = field(default=0, init=False)
    tail: int = field(default=0, init=False)

    def __post_init__(self) -> None:
        self.queue = [None] * self.size

    def enqueue(self, x: Any) -> None:
        self.queue[self.tail] = x

        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> Any:
        x = self.queue[self.head]

        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1

        return x

    def is_empty(self) -> bool:
        return self.head == self.tail
