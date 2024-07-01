from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.queue import Queue


def bfs(g: Graph, s: Vertex) -> None:
    """WC: Θ(V + E).
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
        u: Vertex = q.dequeue()

        for v in g.adj[u]:
            if v.color is Status.UNVISITED:
                v.color = Status.VISITING
                v.d = u.d + 1
                v.pi = u
                q.enqueue(v)

        u.color = Status.VISITED
