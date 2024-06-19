from algorithms.datastructures.graph import Graph, Vertex
from algorithms.datastructures.minimum_priority_queue import (
    MinimumPriorityQueue,
)


def mst_prim(
    g: Graph, w: dict[tuple[Vertex, Vertex], float], r: Vertex
) -> None:
    for u in g.V:
        u.key = float("inf")
        u.pi = None

    r.key = 0
    q = MinimumPriorityQueue(key="key")

    for u in g.V:
        q.insert(u)

    while q:
        u = q.extract_min()

        for v in g.adj[u]:
            if v in q and w[(u, v)] < v.key:
                v.pi = u
                v.key = w[(u, v)]  # Also done by decrease_key(...)
                q.decrease_key(v, w[(u, v)])
