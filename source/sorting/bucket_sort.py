import itertools


def bucket_sort(a: list[float], n: int) -> list[float]:
    b: list[list[float]] = [[] for _ in range(n)]
    for i in range(n):
        x = a[i]
        b[int(n * x)].append(x)

    for i in range(n):
        b[i].sort()

    return list(itertools.chain.from_iterable(b))
