from enum import Enum

from source.datastructures.graph import Graph, Status, Vertex


# 🪭🌬️
TIME = 0


class Classification(Enum):
    TREE = "tree"
    BACK = "back"
    FORWARD = "forward"
    CROSS = "cross"


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

    def visit(g: Graph, u: Vertex) -> None:
        global TIME
        TIME += 1

        u.d = TIME
        u.color = Status.VISITING

        for v in sorted(g.adj[u], key=lambda x: x.name):
            edge = (u, v)

            if v.color is Status.UNVISITED:
                classifications[edge] = Classification.TREE
                v.pi = u
                visit(g, v)
            elif v.color is Status.VISITING:
                classifications[edge] = Classification.BACK
            elif v.d < u.d:
                classifications[edge] = Classification.CROSS
            else:
                classifications[edge] = Classification.FORWARD

        u.color = Status.VISITED
        TIME += 1
        u.f = TIME

    for u in g.V:
        u.color = Status.UNVISITED

    global TIME
    TIME = 0
    classifications: dict[tuple[Vertex, Vertex], Classification] = {}

    for u in g.V:
        if u.color is Status.UNVISITED:
            visit(g, u)

    return classifications
