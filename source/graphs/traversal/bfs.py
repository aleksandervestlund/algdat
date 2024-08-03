from collections.abc import Callable
from typing import Any

from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.queue import Queue


def bfs(
    g: Graph,
    s: Vertex,
    priority: Callable[
        [Vertex], Any
    ] = lambda x: x.name,  #! Not part of pseudocode
) -> None:
    """Breadth First Search.

    Runtimes:
        WC: Θ(V + E).
        BC: Θ(V).
    """
    for u in g.V - {s}:
        u.color = Status.UNVISITED
        u.d = float("inf")
        u.pi = None

    s.color = Status.VISITING
    s.d = 0
    s.pi = None
    q = Queue(len(g.V))
    q.enqueue(s)

    while not q.is_empty():
        u: Vertex = q.dequeue()  # type: ignore
        vertices = sorted(
            g.adj[u], key=priority
        )  #! Not part of the original pseudocode.

        for v in vertices:
            if v.color is Status.UNVISITED:
                v.color = Status.VISITING
                v.d = u.d + 1
                v.pi = u
                q.enqueue(v)

        u.color = Status.VISITED
