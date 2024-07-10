from source.datastructures.graph import Graph, Vertex
from source.graphs.flow.helpers.bfs_labelling import bfs_labelling


def edmond_karp(
    g: Graph, s: Vertex, t: Vertex, cs: dict[tuple[Vertex, Vertex], float]
) -> dict[tuple[Vertex, Vertex], float]:
    """Implementation of the Ford-Fulkerson method.

    Runtime: O(V*E^2).
    """
    cfs = cs.copy()
    fs: dict[tuple[Vertex, Vertex], float] = {}

    for u, v in g.E:
        fs[(u, v)] = 0.0
        fs[(v, u)] = cfs[(u, v)]

    while bfs_labelling(g, s, t, fs, cfs, cs):
        cfp = t.f
        u = t.pi
        v = t

        while u is not None:
            forward = (u, v)
            backward = (v, u)

            if forward in g.E:
                fs[forward] += cfp
                cfs[forward] -= cfp
            else:
                fs[backward] -= cfp
                cfs[backward] += cfp

            v = u
            u = u.pi

    #! Nothing is returned in the pseudocode.
    return {edge: fs[edge] for edge in g.E}
