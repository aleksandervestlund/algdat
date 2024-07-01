from source.datastructures.graph import Graph, Vertex
from source.datastructures.queue import Queue


def bfs_labelling(g: Graph, s: Vertex, t: Vertex) -> bool:
    cfs: dict[tuple[Vertex, Vertex], float] = {}
    fs: dict[tuple[Vertex, Vertex], float] = {}

    for u in g.V:
        u.f = 0.0
        u.pi = None

    s.f = float("inf")
    q = Queue(size=len(g.V))
    q.enqueue(s)

    while not q.is_empty() and t.f == 0.0:
        u: Vertex = q.dequeue()

        for u, v in g.E:
            if (u, v) in g.E:
                cfs[(u, v)] = cfs.get((u, v), 0.0) - fs[(u, v)]
            else:
                cfs[(u, v)] = fs.get((v, u), 0.0)

            if v.f == 0.0 and cfs[(u, v)] > 0.0:
                v.f = min(u.f, cfs[(u, v)])
                v.pi = u
                q.enqueue(v)

    return t.f != 0.0
