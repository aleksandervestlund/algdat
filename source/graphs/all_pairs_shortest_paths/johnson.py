from source.datastructures.graph import Graph, Vertex
from source.graphs.single_source_shortest_paths.bellman_ford import (
    bellman_ford,
)
from source.graphs.single_source_shortest_paths.dijkstra import dijkstra


def johnson(
    g: Graph, w: dict[tuple[Vertex, Vertex], float]
) -> list[list[float]]:
    """Runtime: O(V^2*log(V)+V*E)."""
    g_marked = g.copy()
    s = Vertex("s")
    g_marked.adj[s] = g.V
    bellman_ford(g_marked, w | {(s, v): 0 for v in g.V}, s)

    n = len(g.V)
    vertices = sorted(g.V, key=lambda v: v.name)
    h = [float("inf")] * n
    w_hat: dict[tuple[Vertex, Vertex], float] = {}
    d = [[float("inf")] * n for _ in range(n)]

    for i, v in enumerate(vertices):
        h[i] = v.d

    for edge in g.E:
        u, v = edge
        w_hat[edge] = w[edge] + h[vertices.index(u)] - h[vertices.index(v)]

    for u in g.V:
        dijkstra(g, w_hat, u)

        for v in g.V:
            u_idx = vertices.index(u)
            v_idx = vertices.index(v)
            d[u_idx][v_idx] = v.d + h[v_idx] - h[u_idx]

    return d
