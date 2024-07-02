from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.queue import Queue


# TODO: Make work.


def _find_path(g: Graph, s: Vertex, t: Vertex) -> list[tuple[Vertex, Vertex]]:
    """Modified BFS."""
    for u in g.V - {s}:
        u.color = Status.UNVISITED
        u.d = float("inf")
        u.pi = None

    s.color = Status.VISITING
    s.d = 0
    s.pi = None
    q = Queue(len(g.V))
    q.enqueue(s)
    path: list[tuple[Vertex, Vertex]] = []

    while not q.is_empty():
        u: Vertex = q.dequeue()

        for v in g.adj[u]:
            if v.color is Status.UNVISITED:
                v.color = Status.VISITING
                v.d = u.d + 1
                v.pi = u
                q.enqueue(v)

                if v is t:
                    current = t

                    while (prev := current.pi) is not None:
                        path.insert(0, (prev, current))
                        current = prev

                    return path

        u.color = Status.VISITED

    return path


def ford_fulkerson(
    g: Graph, s: Vertex, t: Vertex, w: dict[tuple[Vertex, Vertex], float]
) -> dict[tuple[Vertex, Vertex], float]:
    """Uses BFS since Dijkstra would have a worse time complexity.
    Runtime: O(V*E^2).
    """
    g_f = Graph()
    g_f.adj = {u: vs.copy() for u, vs in g.adj.items()}
    fs: dict[tuple[Vertex, Vertex], float] = {}
    cfs = w.copy()

    for u, v in g.E:
        fs[(u, v)] = 0.0
        fs[(v, u)] = 0.0
        g_f.adj[v].add(u)
        if (v, u) not in cfs:
            cfs[(v, u)] = float("inf")

    while p := _find_path(g_f, s, t):
        cf_p = min(cfs[e] for e in p)

        for u, v in p:
            fs[(u, v)] += cf_p
            fs[(v, u)] -= cf_p
            cfs[(u, v)] -= cf_p
            cfs[(v, u)] += cf_p
            if cfs[(u, v)] == 0.0:
                g_f.adj[u].remove(v)

    return fs
