def extend_shortest_paths(
    l: list[list[float]],
    w: list[list[float]],
    l_marked: list[list[float]],
    n: int,
) -> None:
    """Θ(n^3)."""
    for i in range(n):
        for j in range(n):
            for k in range(n):
                l_marked[i][j] = min(l_marked[i][j], l[i][k] + w[k][j])
