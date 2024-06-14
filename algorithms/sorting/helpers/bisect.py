def bisect(arr: list[int], p: int, r: int, v: int) -> int | None:
    if p > r:
        return None
    q = (p + r) // 2
    if v == arr[q]:
        return q
    if v < arr[q]:
        return bisect(arr, p, q - 1, v)
    return bisect(arr, q + 1, r, v)
