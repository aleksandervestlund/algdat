from __future__ import annotations

from dataclasses import dataclass, field

from algorithms.status import Status


@dataclass(slots=True)
class Vertex:
    name: str | int

    # Traversal
    color: Status = Status.UNVISITED
    pi: Vertex | None = field(default=None)
    d: float = float("-inf")
    f: float = float("-inf")

    # Minimal Spanning Tree
    p: Vertex | None = field(default=None, repr=False)
    rank: int = field(default=0, repr=False)
    key: float = float("inf")

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return f"Vertex({self.name}, π={self.pi.name if self.pi is not None else None}, key={self.key})"


@dataclass(slots=True)
class Graph:
    adj: dict[Vertex, set[Vertex]] = field(default_factory=dict)

    @property
    def V(self) -> set[Vertex]:
        return set(self.adj)

    @property
    def E(self) -> set[tuple[Vertex, Vertex]]:
        return {(u, v) for u in self.adj for v in self.adj[u]}
