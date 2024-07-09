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

        for edge in g.E:
            u, v = edge

            if edge in g.E:
                cfs[edge] = cfs.get(edge, 0.0) - fs[edge]
            else:
                cfs[edge] = fs.get((v, u), 0.0)

            if v.f == 0.0 and cfs[edge] > 0.0:
                v.f = min(u.f, cfs[edge])
                v.pi = u
                q.enqueue(v)

    return t.f != 0.0
