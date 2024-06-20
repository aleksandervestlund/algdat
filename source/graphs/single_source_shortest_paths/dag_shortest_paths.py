from source.datastructures.graph import Graph, Vertex, topological_sort
from source.graphs.single_source_shortest_paths.helpers.initialize_single_source import (
    initialize_single_source,
)
from source.graphs.single_source_shortest_paths.helpers.relax import relax


def dag_shortest_paths(
    g: Graph, w: dict[tuple[Vertex, Vertex], float], s: Vertex
) -> None:
    topologic = topological_sort(g)
    initialize_single_source(g, s)

    for u in topologic:
        for v in g.adj[u]:
            relax(u, v, w)
