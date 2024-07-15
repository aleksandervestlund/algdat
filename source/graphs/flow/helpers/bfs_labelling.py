from source.datastructures.graph import Graph, Vertex
from source.datastructures.queue import Queue


def bfs_labelling(
    g: Graph,
    s: Vertex,
    t: Vertex,
    fs: dict[tuple[Vertex, Vertex], int],
    cfs: dict[tuple[Vertex, Vertex], int],
    cs: dict[tuple[Vertex, Vertex], int],
) -> bool:
    for u in g.V:
        u.f = 0
        u.pi = None

    s.f = float("inf")
    q = Queue(len(g.V))
    q.enqueue(s)

    while not q.is_empty() and t.f == 0:
        u: Vertex = q.dequeue()
        edges = {edge for edge in g.E if u in edge}

        for edge in edges:
            v = edge[1]
            backward = (v, u)

            if edge in g.E:
                cfs[edge] = cs[edge] - fs[edge]
            else:
                cfs[edge] = fs[backward]

            if cfs[edge] > 0 and v.f == 0:
                v.f = min(u.f, cfs[edge])
                v.pi = u
                q.enqueue(v)

    return t.f != 0
