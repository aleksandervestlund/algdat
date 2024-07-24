from source.sorting.helpers.merge import merge


def merge_sort(a: list[float], p: int, r: int) -> None:
    """Divide and conquer.

    Runtime: Θ(n*log(n)).
    Stable: Yes.
    In-place: No?
    """
    if p >= r - 1:
        return

    q = (p + r) // 2
    merge_sort(a, p, q)
    merge_sort(a, q, r)
    merge(a, p, q, r)
