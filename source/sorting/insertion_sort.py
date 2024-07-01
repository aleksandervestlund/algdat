def insertion_sort(a: list[int], n: int) -> None:
    """BC: Θ(n) (sorted).
    WC: Θ(n^2) (sorted, but reversed).
    AC: Θ(n^2).
    Stable: Yes.
    """
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
