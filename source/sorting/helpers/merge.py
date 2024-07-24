def merge(a: list[float], p: int, q: int, r: int) -> None:
    """Runtime: Θ(n).
    Stable: Yes.
    In-place: No?
    """
    left = a[p:q] + [float("inf")]
    right = a[q:r] + [float("inf")]
    i = 0
    j = 0

    for k in range(p, r):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
