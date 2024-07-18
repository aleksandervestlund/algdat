from dataclasses import dataclass, field
from typing import Any

from source.datastructures.helpers.underflow import UnderflowError


@dataclass(slots=True)
class Stack:
    size: int = field(repr=False)
    stack: list[Any] = field(init=False)
    top: int = field(default=-1, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.size < 1:
            raise ValueError()

        self.stack = [None] * self.size

    def peek(self) -> Any:
        """Runtime: O(1)."""
        if self.stack_empty():
            raise UnderflowError()

        return self.stack[self.top]

    def push(self, x: Any) -> None:
        """Runtime: O(1)."""
        if self.top == self.size - 1:
            raise OverflowError()

        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> Any:
        """Runtime: O(1)."""
        if self.stack_empty():
            raise UnderflowError()

        self.top -= 1
        return self.stack[self.top + 1]

    def multi_pop(self, n: int) -> None:
        """Runtime: Θ(n)."""
        while n and not self.stack_empty():
            self.pop()
            n -= 1

    def stack_empty(self) -> bool:
        """Runtime: O(1)."""
        return self.top == -1
