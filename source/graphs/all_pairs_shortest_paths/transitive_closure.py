from source.datastructures.graph import Graph


def transitive_closure(g: Graph, n: int) -> list[list[bool]]:
    """Also known as Warshall's algorithm.

    Runtime: Θ(n^3).
    """
    t = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n)]
    vertices = sorted(g.V, key=lambda x: x.name)

    for i, u in enumerate(vertices):
        for j, v in enumerate(vertices):
            t[0][i][j] = u is v or (u, v) in g.E

    for k in range(n):
        for i in range(n):
            for j in range(n):
                t[k + 1][i][j] = t[k][i][j] or (t[k][i][k] and t[k][k][j])

    return t[-1]


def transitive_closure_marked(g: Graph, n: int) -> list[list[bool]]:
    vertices = sorted(g.V, key=lambda x: x.name)
    t = [[i is j or (j, i) in g.E for i in vertices] for j in vertices]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                t[i][j] |= t[i][k] and t[k][j]

    return t
