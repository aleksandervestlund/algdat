def insertion_sort(a: list[float], n: int) -> None:
    """Runtimes:
        BC: Θ(n) (sorted).
        WC: Θ(n^2) (sorted in reverse order).
        AC: Θ(n^2).

    Stable: Yes.
    In-place: Yes.
    """
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
