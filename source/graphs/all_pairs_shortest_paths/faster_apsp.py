from source.graphs.all_pairs_shortest_paths.extend_shortest_paths import (
    extend_shortest_paths,
)


def faster_apsp(w: list[list[float]], n: int) -> list[list[float]]:
    l = w
    r = 1

    while r < n - 1:
        m = [[float("inf") for _ in range(n)] for _ in range(n)]
        extend_shortest_paths(l, l, m, n)
        r *= 2
        l = m

    return l
