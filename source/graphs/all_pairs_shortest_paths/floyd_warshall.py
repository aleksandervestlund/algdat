import itertools

from source.datastructures.graph import Vertex


def floyd_warshall(w: list[list[float]], n: int) -> list[list[float]]:
    """Works by considering all vertices as intermediate vertices.

    Runtime: Θ(n^3).
    """
    d = [[[0.0] * n for _ in range(n)] for _ in range(n + 1)]
    d[0] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[k + 1][i][j] = min(d[k][i][j], d[k][i][k] + d[k][k][j])

    return d[-1]


def floyd_warshall_marked(
    w: dict[tuple[Vertex, Vertex], float], n: int
) -> tuple[list[list[float]], list[list[Vertex | None]]]:
    """Runtime: Θ(n^3)."""
    d = [[0.0 if i == j else float("inf") for i in range(n)] for j in range(n)]
    pis: list[list[Vertex | None]] = [[None] * n for _ in range(n)]
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
