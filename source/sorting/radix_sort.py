def radix_sort(a: list[int], d: int) -> list[int]:
    """Θ(d(n+k)).
    Stable: Yes, if `sort` is stable.
    """
    for i in range(d):
        a.sort(key=lambda x: x // 10**i % 10)

    return a


def xidar_non_sort(a: list[int], d: int) -> list[int]:
    for i in range(d - 1, -1, -1):
        a.sort(key=lambda x: x // 10**i % 10)

    return a
