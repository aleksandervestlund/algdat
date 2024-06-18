from typing import Any

from algorithms.underflow import UnderflowError


class Stack:
    def __init__(self, size: int) -> None:
        self.stack: list[Any] = []
        self.size = size
        self.top = -1

    def peek(self) -> Any:
        if self.stack_empty():
            raise UnderflowError()

        return self.stack[self.top]

    def push(self, x: Any) -> None:
        if self.top == self.size:
            raise OverflowError()

        self.top += 1
        self.stack.append(x)

    def pop(self) -> Any:
        if self.stack_empty():
            raise UnderflowError()

        self.top -= 1
        return self.stack[self.top + 1]

    def multi_pop(self, n: int) -> None:
        while n and not self.stack_empty():
            self.pop()
            n -= 1

    def stack_empty(self) -> bool:
        return self.top == -1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.stack})"
