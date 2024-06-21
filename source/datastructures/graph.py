from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Status(Enum):
    UNVISITED = "white"
    VISITING = "gray"
    VISITED = "black"


def topological_sort(g: Graph) -> list[Vertex]:
    """Modifies DFS to find topological order."""

    def dfs_visit(u: Vertex) -> None:
        u.color = Status.VISITED
        for v in g.adj[u]:
            if v.color is Status.UNVISITED:
                dfs_visit(v)
        topologic.append(u)

    topologic: list[Vertex] = []
    for u in g.V:
        u.color = Status.UNVISITED
    for u in g.V:
        if u.color is Status.UNVISITED:
            dfs_visit(u)
    return list(reversed(topologic))


@dataclass(slots=True)
class Vertex:
    name: str | int
    # BFS, DFS, Prim, relax, initialize-single-source
    pi: Vertex | None = field(default=None)
    # BFS, DFS, Bellman-Ford, Dijkstra, Johnson, relax, initailize-single-source
    d: float = field(default=float("-inf"), repr=False)
    # BFS, DFS, traverse
    color: Status = field(default=Status.UNVISITED, repr=False)
    f: float = field(default=float("-inf"), repr=False)  # DFS
    p: Vertex | None = field(default=None, repr=False)  # set
    rank: int = field(default=0, repr=False)  # set
    key: float = field(default=float("inf"))  # Prim

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name}, "
            f"π={self.pi.name if self.pi is not None else None}, d={self.d})"
        )


@dataclass(slots=True, repr=False)
class Graph:
    adj: dict[Vertex, set[Vertex]] = field(default_factory=dict)

    @property
    def V(self) -> set[Vertex]:
        return set(self.adj)

    @property
    def E(self) -> set[tuple[Vertex, Vertex]]:
        return {(u, v) for u, vs in self.adj.items() for v in vs}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.V})"
