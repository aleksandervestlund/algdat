from math import ceil

from source.sorting.helpers.partition import (
    partition_around,
    randomized_partition,
)


def randomized_select(a: list[float], p: int, r: int, i: int) -> float:
    """Find the `i`th smallest element in the array. Divide and conquer.

    Runtimes:
        WC: Θ(n^2).
        AC: Θ(n).
        BC: Θ(n).
    """
    if p == r - 1:
        return a[p]

    q = randomized_partition(a, p, r)
    k = q - p

    if i == k:
        return a[q]
    if i < k:
        return randomized_select(a, p, q, i)
    return randomized_select(a, q + 1, r, i - k)


def select(a: list[float], p: int, r: int, i: int) -> float:
    """Find the `i`th smallest element in the array. Divide and conquer.

    Runtime: O(n).
    """
    while (r - p + 1) % 5 != 0:
        for j in range(p + 1, r + 1):
            if a[p] > a[j]:
                a[p], a[j] = a[j], a[p]

        if i == 1:
            return a[p]

        p += 1
        i -= 1

    g = (r - p + 1) // 5

    for j in range(p, p + g):
        indeces = slice(j, j + 5 * g, g)
        a[indeces] = sorted(a[indeces])

    x = select(a, p + 2 * g, p + 3 * g - 1, ceil(g / 2))
    q = partition_around(a, p, r, x)
    k = q - p + 1

    if i == k:
        return a[q]
    if i < k:
        return select(a, p, q, i)
    return select(a, q + 1, r, i - k)
