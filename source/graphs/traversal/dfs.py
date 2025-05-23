from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.stack import Stack


# Not a big fan of global variables... May Allah promote me to an air conditioner
TIME = 0


def dfs(g: Graph) -> None:
    """Depth First Search.

    Runtime: Θ(V + E).
    """
    for u in g.V:
        u.color = Status.UNVISITED
        u.pi = None

    global TIME
    TIME = 0

    for u in g.V:
        if u.color is Status.UNVISITED:
            dfs_visit(g, u)


def dfs_visit(g: Graph, u: Vertex) -> None:
    global TIME
    TIME += 1

    u.d = TIME
    u.color = Status.VISITING

    for v in g.adj[u]:
        if v.color is Status.UNVISITED:
            v.pi = u
            dfs_visit(g, v)

    u.color = Status.VISITED
    TIME += 1
    u.f = TIME


def iterative_dfs_visit(g: Graph, s: Vertex) -> None:
    for u in g.V - {s}:
        u.color = Status.UNVISITED
        u.pi = None

    s.pi = None
    q = Stack(len(g.V))
    q.push(s)

    while not q.stack_empty():
        u: Vertex = q.peek()  # type: ignore

        if u.color is not Status.UNVISITED:
            u.color = Status.VISITED
            q.pop()
            continue

        u.color = Status.VISITING

        for v in g.adj[u]:
            if v.color is Status.UNVISITED:
                v.pi = u
                q.push(v)
