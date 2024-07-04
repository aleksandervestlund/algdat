from source.datastructures.graph import Graph, Vertex
from source.datastructures.set import find_set, make_set, union


def connected_components(g: Graph) -> None:
    for v in g.V:
        make_set(v)

    for u, v in g.E:
        if find_set(u) is not find_set(v):
            union(u, v)


def same_components(u: Vertex, v: Vertex) -> bool:
    return find_set(u) is find_set(v)
