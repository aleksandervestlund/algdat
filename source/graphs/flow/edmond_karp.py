from source.datastructures.graph import Graph, Vertex
from source.graphs.flow.helpers.bfs_labelling import bfs_labelling


def edmond_karp(g: Graph, s: Vertex, t: Vertex) -> None:
    f: dict[tuple[Vertex, Vertex], float] = {}

    for u, v in g.E:
        f[(u, v)] = 0.0
        f[(v, u)] = 0.0

    while bfs_labelling(g, s, t):
        cfp = t.f
        u = t.pi
        v = t

        while u is not None:
            if (u, v) in g.E:
                f[(u, v)] = f.get((u, v), 0.0) + cfp  # type: ignore
            else:
                f[(v, u)] = f.get((v, u), 0.0) - cfp  # type: ignore

            u = u.pi
            v = u
