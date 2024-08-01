from source.datastructures.graph import Graph, Vertex
from source.datastructures.set import make_set, union
from source.graphs.minimal_spanning_tree.components import same_components


def mst_kruskal(
    g: Graph, w: dict[tuple[Vertex, Vertex], float]
) -> set[tuple[Vertex, Vertex]]:
    """Grows the tree by connecting the cheapest edge that does not form
    a cycle.

    Runtime: O(E*log(V)).
    """
    a: set[tuple[Vertex, Vertex]] = set()

    for v in g.V:
        make_set(v)

    edges = sorted(g.E, key=lambda x: w[x])  # O(E*log(V))

    for edge in edges:
        u, v = edge

        if not same_components(u, v):
            a.add(edge)
            union(u, v)

    return a
