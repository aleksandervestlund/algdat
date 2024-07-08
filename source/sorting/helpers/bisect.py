def bisect(a: list[int], p: int, r: int, v: int) -> int | None:
    """Also known as binary search.

    Runtime: O(log(n)).
    """
    if p > r:
        return None

    q = (p + r) // 2

    if v == a[q]:
        return q
    if v < a[q]:
        return bisect(a, p, q - 1, v)
    return bisect(a, q + 1, r, v)
