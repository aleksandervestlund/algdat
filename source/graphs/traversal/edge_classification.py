from enum import StrEnum, auto

from source.datastructures.graph import Graph, Status, Vertex


class Classification(StrEnum):
    TREE = auto()
    BACK = auto()
    FORWARD = auto()
    CROSS = auto()


def edge_classification(
    g: Graph,
) -> dict[tuple[Vertex, Vertex], Classification]:
    """Modified DFS. Orders edges based on name.

    Edge classification:
        Tree-edge: Edges in the DF-forest.
        Back-edge: Edges to predecessor in DF-forest.
        Forward-edge: Edges to descendants in DF-forest.
        Cross-edge: All remaining edges.
    """

    def visit(g: Graph, u: Vertex, time: int) -> int:
        time += 1
        u.d = time
        u.color = Status.VISITING

        for v in sorted(g.adj[u], key=lambda x: x.name):
            edge = (u, v)

            if v.color is Status.UNVISITED:
                classifications[edge] = Classification.TREE
                v.pi = u
                time = visit(g, v, time)
            elif v.color is Status.VISITING:
                classifications[edge] = Classification.BACK
            elif v.d < u.d:
                classifications[edge] = Classification.CROSS
            else:
                classifications[edge] = Classification.FORWARD

        u.color = Status.VISITED
        time += 1
        u.f = time
        return time

    time = 0
    classifications: dict[tuple[Vertex, Vertex], Classification] = {}

    for u in sorted(g.V, key=lambda x: x.name):
        if u.color is Status.UNVISITED:
            time = visit(g, u, time)

    return classifications
