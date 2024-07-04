from source.datastructures.graph import Graph, Vertex
from source.datastructures.set import find_set, make_set, union


def mst_kruskal(
    g: Graph, w: dict[tuple[Vertex, Vertex], float]
) -> set[tuple[Vertex, Vertex]]:
    """O(E*log(V))."""
    a: set[tuple[Vertex, Vertex]] = set()

    for v in g.V:
        make_set(v)

    edges = sorted(g.E, key=lambda x: w[x])  # O(E*log(E))

    for u, v in edges:
        if find_set(u) is not find_set(v):
            a.add((u, v))
            union(u, v)

    return a
