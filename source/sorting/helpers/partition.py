import math
import random


def partition(a: list[float], p: int, r: int) -> int:
    """Runtime: O(n).
    Stable: No.
    In-place: Yes.
    """
    x = a[r - 1]
    i = p - 1

    for j in range(p, r - 1):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[r - 1] = a[r - 1], a[i + 1]
    return i + 1


def randomized_partition(a: list[float], p: int, r: int) -> int:
    """Runtime: O(n).
    Stable: No.
    In-place: Yes.
    """
    i = random.randint(p, r - 1)
    a[i], a[r - 1] = a[r - 1], a[i]
    return partition(a, p, r)


def partition_around(a: list[float], p: int, r: int, x: float) -> int:
    """Runtime: O(n).
    Stable: No.
    In-place: Yes.
    """
    if x not in a:
        raise ValueError()

    i = 0
    while a[i] != x:
        i += 1
    # i = a.index(x)

    a[i], a[r - 1] = a[r - 1], a[i]
    return partition(a, p, r)


def good_partition(a: list[float], p: int, r: int) -> int:
    """Runtime: O(n).
    Stable: No.
    In-place: Yes.
    """
    from source.sorting.helpers.select import select  # avoid circular import

    n = r - p
    m = math.ceil(n / 5)
    b: list[float] = []

    for i in range(m):
        q = p + 5 * i
        indeces = slice(q, q + 5)
        a[indeces] = sorted(a[indeces])
        b.append(a[q + 2])

    x = select(b, 0, m, m // 2)
    return partition_around(a, p, r, x)
