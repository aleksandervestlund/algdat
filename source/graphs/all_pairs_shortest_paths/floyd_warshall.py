import itertools

from source.datastructures.graph import Vertex


def floyd_warshall(w: list[list[float]], n: int) -> list[list[float]]:
    """Θ(n^3)."""
    d = [[[0.0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    d[0] = w

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                d[k][i][j] = min(
                    d[k - 1][i][j], d[k - 1][i][k] + d[k - 1][k][j]
                )

    return d[n - 1]


def floyd_warshall_marked(
    w: dict[tuple[Vertex, Vertex], float], n: int
) -> tuple[list[list[float]], list[list[Vertex | None]]]:
    """Θ(n^3)."""
    d = [[0.0 if i == j else float("inf") for i in range(n)] for j in range(n)]
    pis: list[list[Vertex | None]] = [
        [None for _ in range(n)] for _ in range(n)
    ]
    vertices = sorted(
        set(itertools.chain.from_iterable(w)), key=lambda x: x.name
    )

    for (u, v), value in w.items():
        u_idx = vertices.index(u)
        v_idx = vertices.index(v)
        d[u_idx][v_idx] = value
        pis[u_idx][v_idx] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > (distance := d[i][k] + d[k][j]):
                    d[i][j] = distance
                    pis[i][j] = pis[k][j]

    return d, pis
