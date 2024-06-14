from algorithms.sorting.helpers.partition import partition, randomized_partition


def quick_sort(arr: list[int], p: int, r: int) -> None:
    if p >= r - 1:
        return
    q = partition(arr, p, r)
    quick_sort(arr, p, q)
    quick_sort(arr, q + 1, r)


def randomized_quick_sort(arr: list[int], p: int, r: int) -> None:
    if p >= r - 1:
        return
    q = randomized_partition(arr, p, r)
    randomized_quick_sort(arr, p, q)
    randomized_quick_sort(arr, q + 1, r)
