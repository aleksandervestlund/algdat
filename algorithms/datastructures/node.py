from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    key: int
    prev: Node | None = None
    next: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.key})"
        # return f"{self.__class__.__name__}({self.key})"
