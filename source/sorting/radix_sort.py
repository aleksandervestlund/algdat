def radix_sort(a: list[int], d: int) -> list[int]:
    """Runtime: Θ(d(n+k)).
    Stable: Yes, if `sort` is stable.
    In-place: No.
    """
    _validate_range(a, d)  #! Not part of pseudocode.

    for i in range(d):
        a.sort(key=lambda x: x // 10**i % 10)

    return a


def xidar_non_sort(a: list[int], d: int) -> list[int]:
    for i in range(d - 1, -1, -1):
        a.sort(key=lambda x: x // 10**i % 10)

    return a


def _validate_range(a: list[int], d: int) -> None:
    if not all(0 <= x < 10**d for x in a):
        raise ValueError("Elements should be in the range [0, 10^d).")
