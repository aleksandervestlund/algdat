from source.sorting.helpers.partition import (
    partition,
    randomized_partition,
)


def quicksort(a: list[int], p: int, r: int) -> None:
    if p >= r - 1:
        return

    q = partition(a, p, r)
    quicksort(a, p, q)
    quicksort(a, q + 1, r)


def randomized_quicksort(a: list[int], p: int, r: int) -> None:
    if p >= r - 1:
        return

    q = randomized_partition(a, p, r)
    randomized_quicksort(a, p, q)
    randomized_quicksort(a, q + 1, r)
