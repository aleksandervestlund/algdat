from source.sorting.helpers.merge import merge


def merge_sort(a: list[int], p: int, r: int) -> None:
    """O(n*lg(n))."""
    if p >= r - 1:
        return

    q = (p + r) // 2
    merge_sort(a, p, q)
    merge_sort(a, q, r)
    merge(a, p, q, r)
