def bisect(a: list[float], p: int, r: int, v: float) -> int | None:
    """Also known as binary search.

    Runtime: O(log(n)).
    """
    if p > r:
        return None  # I would prefer -1, but the pseudocode uses None.

    q = (p + r) // 2

    if v == a[q]:
        return q
    if v < a[q]:
        return bisect(a, p, q - 1, v)
    return bisect(a, q + 1, r, v)
