from source.datastructures.graph import Graph, Vertex
from source.datastructures.priority_queue import PriorityQueue
from source.graphs.single_source_shortest_paths.helpers.initialize_single_source import (
    initialize_single_source,
)
from source.graphs.single_source_shortest_paths.helpers.relax import relax


def dijkstra(g: Graph, w: dict[tuple[Vertex, Vertex], int], s: Vertex) -> None:
    initialize_single_source(g, s)
    S = set()
    q = PriorityQueue(key="d")

    for u in g.V:
        q.insert(u)

    while q:
        u = q.extract_min()
        S.add(u)

        for v in g.adj[u]:
            old = v.d
            relax(u, v, w)

            if v.d != old:
                q.decrease_key(v, v.d)
