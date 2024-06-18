from __future__ import annotations

from dataclasses import dataclass, field

from algorithms.status import Status


@dataclass
class Vertex:
    number: int
    color = Status.UNVISITED
    pi: Vertex | None = None
    d = float("-inf")
    f = float("-inf")

    def __repr__(self) -> str:
        return (
            f"{self.number}: c={self.color.value:>5}, d={self.d:>3}, "
            f"f={self.f:>4}, π={self.pi.number if self.pi else None}"
        )

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vertex) and hash(other) == hash(self)


@dataclass
class Graph:
    adj: dict[Vertex, set[Vertex]] = field(default_factory=dict)

    @property
    def v(self) -> set[Vertex]:
        return set(self.adj)

    def __repr__(self) -> str:
        separator = "\n    "
        return (
            f"{self.__class__.__name__}({separator}"
            + separator.join(str(elem) for elem in self.v)
            + "\n)"
        )
