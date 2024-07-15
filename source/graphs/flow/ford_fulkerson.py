from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.queue import Queue


def ford_fulkerson(
    g: Graph, s: Vertex, t: Vertex, cfs: dict[tuple[Vertex, Vertex], int]
) -> dict[tuple[Vertex, Vertex], int]:
    """Ford-Fulkerson does not specify which shortest path algorithm to
    use. This implementation uses BFS since Dijkstra would have a worse
    time complexity. Therefore, it does not have guaranteed polynomial
    time complexity. If the weights are real numbers, the algorithm may
    never terminate.
    Nodes visited in last iteration are part of the minimal cut.
    """
    g_f = Graph()
    g_f.adj = {u: adjacencies.copy() for u, adjacencies in g.adj.items()}
    fs = {edge: 0 for edge in g.E}

    while (path := find_path(g_f, s, t)) is not None:
        cfp = min(cfs[edge] for edge in path)

        for forward in path:
            backward = (forward[1], forward[0])

            if forward in g.E:
                fs[forward] += cfp
                cfs[forward] -= cfp
            else:
                cfs[backward] += cfp

            #! Not part of the pseudocode, but necessary to update the graph.
            for edge in (forward, backward):
                u, v = edge

                if edge not in g.E:
                    g_f.adj[u].add(v)
                    cfs[edge] = cfp
                elif cfs[edge] == 0.0:
                    g_f.adj[u].discard(v)
                    cfs.pop(edge)

    return fs


def find_path(
    g: Graph, s: Vertex, t: Vertex
) -> list[tuple[Vertex, Vertex]] | None:
    """Modified BFS. Not part of the pseudocode, but necessary to find a
    path from the source to the sink.
    """
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
