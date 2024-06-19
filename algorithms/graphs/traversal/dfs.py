from algorithms.datastructures.graph import Graph, Vertex
from algorithms.datastructures.stack import Stack
from algorithms.status import Status


# Should probably use a class to store the global variable...
TIME = 0


def dfs(g: Graph) -> None:
    for u in g.V:
        u.color = Status.UNVISITED
        u.pi = None  # Already None by default...

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
        u = q.peek()

        if u.color is not Status.UNVISITED:
            u.color = Status.VISITED
            q.pop()
            continue

        u.color = Status.VISITING

        for v in g.adj[u]:
            if v.color is Status.UNVISITED:
                v.pi = u
                q.push(v)
