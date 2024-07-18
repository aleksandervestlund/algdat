from source.datastructures.graph import Graph, Vertex
from source.graphs.flow.helpers.bfs_labelling import bfs_labelling


def edmond_karp(
    g: Graph, s: Vertex, t: Vertex, cs: dict[tuple[Vertex, Vertex], int]
) -> dict[tuple[Vertex, Vertex], int]:
    """Implementation of the Ford-Fulkerson method.

    Runtime: O(V*E^2).
    """
    cfs = cs.copy()
    fs = {edge: 0 for edge in g.E}

    while bfs_labelling(g, s, t, fs, cfs, cs):
        cfp: int = t.f  # type: ignore
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

    return fs
