from source.sorting.helpers.partition import partition, randomized_partition


def quicksort(a: list[int], p: int, r: int) -> None:
    """Divide and conquer.

    Runtimes:
        BC: Θ(n*log(n)).
        AC: Θ(n*log(n)).
        WC: Θ(n^2) (sorted in reverse order).
    Stable: No.
    """
    if p >= r - 1:
        return

    q = partition(a, p, r)
    quicksort(a, p, q)
    quicksort(a, q + 1, r)


def randomized_quicksort(a: list[int], p: int, r: int) -> None:
    """Divide and conquer.

    Runtime: Θ(n*log(n)).
    Stable: No.
    """
    if p >= r - 1:
        return

    q = randomized_partition(a, p, r)
    randomized_quicksort(a, p, q)
    randomized_quicksort(a, q + 1, r)
