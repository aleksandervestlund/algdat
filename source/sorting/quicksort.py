from source.sorting.helpers.partition import partition, randomized_partition


def quicksort(a: list[int], p: int, r: int) -> None:
    """Best-case: Θ(n*lg(n)) (sorted).
    Worst-case: Θ(n^2) (sorted, but reversed).
    Average-case: Θ(n*lg(n)).
    In general: Ω(n*lg(n)), O(n^2), Θ(?).
    """
    if p >= r - 1:
        return

    q = partition(a, p, r)
    quicksort(a, p, q)
    quicksort(a, q + 1, r)


def randomized_quicksort(a: list[int], p: int, r: int) -> None:
    """Best-case: Θ(n*lg(n)).
    Worst-case: Θ(n*lg(n)).
    Average-case: Θ(n*lg(n)).
    In general: Θ(n*lg(n)).
    """
    if p >= r - 1:
        return

    q = randomized_partition(a, p, r)
    randomized_quicksort(a, p, q)
    randomized_quicksort(a, q + 1, r)
