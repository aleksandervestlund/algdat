from source.datastructures.graph import Graph, Vertex
from source.datastructures.set import find_set, make_set, union


def connected_components(g: Graph) -> None:
    """Creates a spanning tree, however, it does not guarantee that the
    tree is minimal.

    Runtime: O(E*log(V)).
    """
    for v in g.V:
        make_set(v)

    for u, v in g.E:
        if not same_components(u, v):
            union(u, v)


def same_components(u: Vertex, v: Vertex) -> bool:
    """Runtime: O(1)."""
    return find_set(u) is find_set(v)
