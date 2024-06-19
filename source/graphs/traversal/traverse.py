from source.datastructures.graph import Graph, Vertex
from source.helpers.status import Status


def traverse(g: Graph, u: Vertex) -> None:
    print(u)

    if (adjacent := g.adj.get(u)) is None:
        return
    del g.adj[u]

    for v in adjacent:
        traverse(g, v)

    g.adj[u] = adjacent


def traverse_2(g: Graph, u: Vertex) -> None:
    print(u)
    u.color = Status.VISITING

    for v in g.adj[u]:
        if v.color is Status.UNVISITED:
            traverse_2(g, v)

    u.color = Status.VISITED
