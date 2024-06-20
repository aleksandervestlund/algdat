from source.graphs.all_pairs_shortest_paths.extend_shortest_paths import (
    extend_shortest_paths,
)


def slow_apsp(
    w: list[list[float]], l_zero: list[list[float]], n: int
) -> list[list[float]]:
    l = l_zero

    for _ in range(n - 1):
        m = [[float("inf") for _ in range(n)] for _ in range(n)]
        extend_shortest_paths(l, w, m, n)
        l = m

    return l
