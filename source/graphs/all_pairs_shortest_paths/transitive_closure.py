from source.datastructures.graph import Graph


def transitive_closure(g: Graph, n: int) -> list[list[int]]:
    """Θ(n^3)."""
    t = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    vertices = sorted(g.V, key=lambda x: x.name)

    for i, u in enumerate(vertices):
        for j, v in enumerate(vertices):
            t[0][i][j] = int(u is v or (u, v) in g.E)

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                t[k][i][j] = int(
                    t[k - 1][i][j] or (t[k - 1][i][k] and t[k - 1][k][j])
                )

    return t[-1]


def transitive_closure_marked(g: Graph, n: int) -> list[list[int]]:
    vertices = sorted(g.V, key=lambda x: x.name)
    t = [[int(i is j or (j, i) in g.E) for i in vertices] for j in vertices]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                t[i][j] = int(t[i][j] or (t[i][k] and t[k][j]))

    return t
