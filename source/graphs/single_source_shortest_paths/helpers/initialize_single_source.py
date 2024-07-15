from source.datastructures.graph import Graph, Vertex


def initialize_single_source(g: Graph, s: Vertex) -> None:
    """Runtime: Θ(V)."""
    for v in g.V:
        v.d = float("inf")
        v.pi = None

    s.d = 0
