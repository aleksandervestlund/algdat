from source.datastructures.graph import Graph, Vertex
from source.graphs.single_source_shortest_paths.bellman_ford import (
    bellman_ford,
)
from source.graphs.single_source_shortest_paths.dijkstra import dijkstra


def johnson(
    g: Graph, w: dict[tuple[Vertex, Vertex], float]
) -> list[list[float]]:
    vertices = sorted(g.V, key=lambda v: v.name)

    h = [float("inf") for _ in range(len(vertices))]
    w_hat: dict[tuple[Vertex, Vertex], float] = {}

    for s in vertices:
        bellman_ford(g, w, s)

        for v in g.V:
            v_idx = vertices.index(v)
            h[v_idx] = min(v.d, h[v_idx])

    for u, v in g.E:
        w_hat[(u, v)] = w[(u, v)] + h[vertices.index(u)] - h[vertices.index(v)]

    n = len(g.V)
    d = [[float("inf") for _ in range(n)] for _ in range(n)]

    for u in g.V:
        dijkstra(g, w_hat, u)

        for v in g.V:
            u_idx = vertices.index(u)
            v_idx = vertices.index(v)
            d[u_idx][v_idx] = v.d + h[v_idx] - h[u_idx]

    return d
