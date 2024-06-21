def insertion_sort(a: list[int], n: int) -> None:
    """Best-case: Θ(n) (sorted).
    Worst-case: Θ(n^2) (sorted, but reversed).
    Average-case: Θ(n^2).
    In general: Ω(n), O(n^2), Θ(?).
    """
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
