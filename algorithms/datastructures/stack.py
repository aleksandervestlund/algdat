from typing import Any


class UnderflowError(Exception):
    pass


class Stack:
    def __init__(self, size: int) -> None:
        self.stack: list[Any] = []
        self.size = size
        self.top = -1

    def push(self, x: Any) -> None:
        if self.top == self.size:
            raise OverflowError()
        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> Any:
        if self.is_empty():
            raise UnderflowError()
        self.top -= 1
        return self.stack[self.top + 1]

    def is_empty(self) -> bool:
        return self.top == -1
