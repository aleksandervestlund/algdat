def radix_sort(arr: list[int], d: int) -> list[int]:
    for i in range(d):
        arr = sorted(arr, key=lambda x: x // 10**i % 10)
    return arr


def xidar_non_sort(arr: list[int], d: int) -> list[int]:
    for i in range(d, -1, -1):
        arr = sorted(arr, key=lambda x: x // 10**i % 10)
    return arr
