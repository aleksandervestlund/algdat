import itertools


def bucket_sort(a: list[float], n: int) -> list[float]:
    """BC: Θ(n).
    AC: Θ(n).
    WC: Θ(n^2).
    Stable: Yes.
    """
    b: list[list[float]] = [[] for _ in range(n)]

    for i in range(n):
        x = a[i]
        b[int(n * x)].append(x)

    for i in range(n):
        b[i].sort()

    return list(itertools.chain.from_iterable(b))
