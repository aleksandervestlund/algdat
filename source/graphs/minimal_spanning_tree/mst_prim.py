from source.datastructures.graph import Graph, Vertex
from source.datastructures.priority_queue import PriorityQueue


def mst_prim(
    g: Graph, w: dict[tuple[Vertex, Vertex], float], r: Vertex
) -> None:
    """O(E*log(V))."""
    for u in g.V:
        u.key = float("inf")
        u.pi = None

    r.key = 0
    q = PriorityQueue(key="key")

    for u in g.V:
        q.insert(u)

    while q:
        u = q.extract_min()

        for v in g.adj[u]:
            if v in q and w[(u, v)] < v.key:
                v.pi = u
                # v.key = w[(u, v)]
                q.decrease_key(v, w[(u, v)])
