import math

from algorithms.sorting.helpers.partition import (
    partition_around,
    randomized_partition,
)


def randomized_select(arr: list[int], p: int, r: int, i: int) -> int:
    if p == r - 1:
        return arr[p]
    q = randomized_partition(arr, p, r)
    k = q - p
    if i == k:
        return arr[q]
    if i < k:
        return randomized_select(arr, p, q, i)
    return randomized_select(arr, q + 1, r, i - k)


def select(arr: list[int], p: int, r: int, i: int) -> int:
    while (r - p + 1) % 5 != 0:
        for j in range(p + 1, r + 1):
            if arr[p] > arr[j]:
                arr[p], arr[j] = arr[j], arr[p]
        if i == 1:
            return arr[p]
        p += 1
        i += 1
    g = (r - p) // 5
    for j in range(p, p + g):
        (
            arr[j + 0 * g],
            arr[j + 1 * g],
            arr[j + 2 * g],
            arr[j + 3 * g],
            arr[j + 4 * g],
        ) = sorted(
            (
                arr[j + 0 * g],
                arr[j + 1 * g],
                arr[j + 2 * g],
                arr[j + 3 * g],
                arr[j + 4 * g],
            )
        )
    x = select(arr, p + 2 * g, p + 3 * g - 1, math.ceil(g / 2))
    q = partition_around(arr, p, r, x)
    k = q - p + 1
    if i == k:
        return arr[q]
    if i < k:
        return select(arr, p, q, i)
    return select(arr, q + 1, r, i - k)
