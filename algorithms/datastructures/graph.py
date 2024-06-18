from __future__ import annotations

from dataclasses import dataclass, field

from algorithms.status import Status


@dataclass(slots=True)
class Vertex:
    number: int
    color = Status.UNVISITED
    pi: Vertex | None = field(default=None, repr=False)
    d = float("-inf")
    f = float("-inf")

    def __hash__(self) -> int:
        return id(self)


@dataclass(slots=True)
class Graph:
    adj: dict[Vertex, set[Vertex]] = field(default_factory=dict)

    @property
    def v(self) -> set[Vertex]:
        return set(self.adj)
