from algorithms.sorting.helpers.merge import merge


def merge_sort(arr: list[int], p: int, r: int) -> None:
    if p >= r - 1:
        return
    q = (p + r) // 2
    merge_sort(arr, p, q)
    merge_sort(arr, q, r)
    merge(arr, p, q, r)
