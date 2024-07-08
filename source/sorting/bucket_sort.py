import itertools

from source.sorting.insertion_sort import insertion_sort


def bucket_sort(a: list[float], n: int) -> list[float]:
    """Uses `insertion_sort` to sort the buckets.

    Runtimes:
        BC: Θ(n).
        AC: Θ(n).
        WC: Θ(n^2) (all elements in the same bucket).
    Stable: Yes.
    """
    b: list[list[float]] = [[] for _ in range(n)]

    for i in range(n):
        x = a[i]
        b[int(n * x)].append(x)

    for i in range(n):
        insertion_sort(b[i], len(b[i]))

    return list(itertools.chain.from_iterable(b))
