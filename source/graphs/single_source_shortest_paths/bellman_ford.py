from source.datastructures.graph import Graph, Vertex
from source.graphs.single_source_shortest_paths.helpers.initialize_single_source import (
    initialize_single_source,
)
from source.graphs.single_source_shortest_paths.helpers.relax import relax


def bellman_ford(
    g: Graph, w: dict[tuple[Vertex, Vertex], float], s: Vertex
) -> bool:
    """Works by relaxing all edges `|V|-1` times.

    Runtime: Θ(V*E).
    """
    initialize_single_source(g, s)

    for _ in range(len(g.V) - 1):
        for u, v in g.E:
            relax(u, v, w)

    # for u, v in g.E:
    #     if v.d > u.d + weight:
    #         return False
    # return True
    return not any(v.d > u.d + w[(u, v)] for u, v in g.E)
