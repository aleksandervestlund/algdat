from __future__ import annotations

from dataclasses import dataclass, field

from algorithms.status import Status


@dataclass(slots=True)
class Vertex:
    name: str | int
    color: Status = field(default=Status.UNVISITED, repr=False)
    pi: Vertex | None = field(default=None)
    p: Vertex | None = field(default=None, repr=False)
    d: float = field(default=float("-inf"), repr=False)
    f: float = field(default=float("-inf"), repr=False)
    rank: int = field(default=0, repr=False)
    key: float = field(default=float("inf"))

    def __hash__(self) -> int:
        return id(self)


@dataclass(slots=True)
class Graph:
    adj: dict[Vertex, set[Vertex]] = field(default_factory=dict)

    @property
    def V(self) -> set[Vertex]:
        return set(self.adj)

    @property
    def E(self) -> set[tuple[Vertex, Vertex]]:
        return {(u, v) for u in self.adj for v in self.adj[u]}
