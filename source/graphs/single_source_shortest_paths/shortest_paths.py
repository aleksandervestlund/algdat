from source.datastructures.graph import Graph, Vertex
from source.graphs.single_source_shortest_paths.bellman_ford import (
    bellman_ford,
)
from source.graphs.single_source_shortest_paths.dag_shortest_paths import (
    dag_shortest_paths,
)
from source.graphs.single_source_shortest_paths.dijkstra import dijkstra
from source.graphs.traversal.edge_classification import (
    Classification,
    edge_classification,
)


def shortest_paths(
    g: Graph, w: dict[tuple[Vertex, Vertex], float], s: Vertex
) -> None:
    """Not part of curriculum and no given pseudocode."""
    if not any(
        classification is Classification.BACK
        for classification in edge_classification(g).values()
    ):
        dag_shortest_paths(g, w, s)
    elif all(weight >= 0 for weight in w.values()):
        dijkstra(g, w, s)
    elif not bellman_ford(g, w, s):
        raise ValueError("Negative cycle.")
