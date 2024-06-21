from dataclasses import dataclass, field
from typing import Any

from source.datastructures.helpers.underflow import UnderflowError


@dataclass(slots=True)
class Stack:
    size: int = field(repr=False)
    stack: list[Any] = field(default_factory=list)
    top: int = field(default=-1, init=False, repr=False)

    def peek(self) -> Any:
        """O(1)."""
        if self.stack_empty():
            raise UnderflowError()

        return self.stack[self.top]

    def push(self, x: Any) -> None:
        """O(1)."""
        if self.top == self.size:
            raise OverflowError()

        self.top += 1
        self.stack.append(x)

    def pop(self) -> Any:
        """O(1)."""
        if self.stack_empty():
            raise UnderflowError()

        self.top -= 1
        return self.stack[self.top + 1]

    def multi_pop(self, n: int) -> None:
        """Θ(n)."""
        while n and not self.stack_empty():
            self.pop()
            n -= 1

    def stack_empty(self) -> bool:
        """O(1)."""
        return self.top == -1
