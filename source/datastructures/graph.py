from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


def topological_sort(g: Graph) -> list[Vertex]:
    """Modifies DFS to find topological order.

    Runtime: Θ(V+E).
    """

    def dfs_visit(u: Vertex) -> None:
        u.color = Status.VISITED
        for v in g.adj[u]:
            if v.color is Status.UNVISITED:
                dfs_visit(v)
        topologic.insert(0, u)

    topologic: list[Vertex] = []
    for u in g.V:
        u.color = Status.UNVISITED
    for u in g.V:
        if u.color is Status.UNVISITED:
            dfs_visit(u)
    return topologic


class Status(Enum):
    UNVISITED = "white"
    VISITING = "gray"
    VISITED = "black"


@dataclass(slots=True)
class Vertex:
    name: str | int
    # BFS, DFS, Prim, relax, initialize-single-source
    pi: Vertex | None = field(default=None)  # predecessor
    # BFS, DFS, Bellman-Ford, Dijkstra, Johnson, relax, initailize-single-source
    d: float = field(default=float("-inf"), repr=False)  # Discover time
    # BFS, DFS, traverse
    color: Status = field(default=Status.UNVISITED, repr=False)
    f: float = field(default=float("-inf"), repr=False)  # DFS; finish time
    p: Vertex | None = field(default=None, repr=False)  # set; parent
    rank: int = field(default=0, repr=False)  # set
    key: float = field(default=float("inf"))  # Prim

    def __hash__(self) -> int:
        """Used for hashing in dictionaries and sets."""
        return hash(self.name)

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

    def copy(self) -> Graph:
        """Returns a shallow copy of the graph."""
        return self.__class__(
            {u: adjacencies.copy() for u, adjacencies in self.adj.items()}
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.V})"
