from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    key: Any
    prev: Node | None = None
    next: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.key})"
