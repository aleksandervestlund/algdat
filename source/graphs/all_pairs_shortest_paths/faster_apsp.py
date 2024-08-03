from source.graphs.all_pairs_shortest_paths.extend_shortest_paths import (
    extend_shortest_paths,
)


def faster_apsp(w: list[list[float]], n: int) -> list[list[float]]:
    """Works in the same way as the slow version, but considers all
    paths of length `2^0`, then all paths of length `2^1`, and so on.

    Runtime: Θ(n^3*log(n)).
    """
    l = w
    r = 1

    while r < n - 1:
        m = [[float("inf")] * n for _ in range(n)]
        extend_shortest_paths(l, l, m, n)
        r *= 2
        l = m

    return l
