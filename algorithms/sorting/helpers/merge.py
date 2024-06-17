def merge(a: list[int], p: int, q: int, r: int) -> None:
    left = a[p:q] + [float("inf")]
    right = a[q:r] + [float("inf")]
    i = 0
    j = 0

    for k in range(p, r):
        if left[i] <= right[j]:
            a[k] = left[i]  # type: ignore
            i += 1
        else:
            a[k] = right[j]  # type: ignore
            j += 1
