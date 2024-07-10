from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.queue import Queue


def find_path(
    g: Graph, s: Vertex, t: Vertex
) -> list[tuple[Vertex, Vertex]] | None:
    """Modified BFS."""
    for u in g.V:
        u.color = Status.UNVISITED
        u.pi = None
    s.color = Status.VISITING
    q = Queue(len(g.V))
    q.enqueue(s)
    while not q.is_empty():
        u: Vertex = q.dequeue()
        for v in sorted(g.adj[u], key=lambda x: x.name):
            if v.color is not Status.UNVISITED:
                continue
            v.color = Status.VISITING
            v.pi = u
            q.enqueue(v)
            if v is not t:
                continue
            path: list[tuple[Vertex, Vertex]] = []
            current = t
            while (prev := current.pi) is not None:
                path.insert(0, (prev, current))
                current = prev
            return path
        u.color = Status.VISITED
    return None


def ford_fulkerson(
    g: Graph, s: Vertex, t: Vertex, cs: dict[tuple[Vertex, Vertex], float]
) -> dict[tuple[Vertex, Vertex], float]:
    """This implementation uses BFS since Dijkstra would have a worse
    time complexity. Ford-Fulkerson does not specify which shortest path
    algorithm to use. Therefore, it does not have guaranteed polynomial
    time complexity.
    Nodes visited in last iteration are part of the minimal cut.
    """
    g_f = Graph()
    g_f.adj = {key: value.copy() for key, value in g.adj.items()}
    cfs = cs.copy()
    fs: dict[tuple[Vertex, Vertex], float] = {}

    for u, v in g.E:
        fs[(u, v)] = 0.0
        fs[(v, u)] = cfs[(u, v)]

    while (path := find_path(g_f, s, t)) is not None:
        cfp = min(cfs[edge] for edge in path)

        for edge in path:
            backward = (edge[1], edge[0])

            if edge in g.E:
                fs[edge] += cfp
                cfs[edge] -= cfp
            else:
                fs[backward] -= cfp
                cfs[backward] += cfp

            # Not part of the pseudocode, but necessary to update the graph.
            for e in (edge, backward):
                u, v = e

                if e not in g.E:
                    g_f.adj[u].add(v)
                    cfs[e] = cfp
                elif cfs[e] == 0.0:
                    g_f.adj[u].remove(v)
                    cfs.pop(e)

    return {edge: fs[edge] for edge in g.E}
