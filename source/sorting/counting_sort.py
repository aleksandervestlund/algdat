def counting_sort(a: list[int], n: int, k: int) -> list[int]:
    """Θ(n+k).
    Stable: Yes.
    """
    b = [0] * n
    c = [0] * (k + 1)

    for i in range(n):
        c[a[i]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1

    return b
