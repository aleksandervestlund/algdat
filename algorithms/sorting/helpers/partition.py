from random import randint


def partition(arr: list[int], p: int, r: int) -> int:
    x = arr[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r - 1] = arr[r - 1], arr[i + 1]
    return i + 1


def randomized_partition(arr: list[int], p: int, r: int) -> int:
    i = randint(p, r - 1)
    arr[i], arr[r - 1] = arr[r - 1], arr[i]
    return partition(arr, p, r)


def partition_around(arr: list[int], p: int, r: int, x: int) -> int:
    if x not in arr:
        raise ValueError()

    i = 0
    while arr[i] != x:
        i += 1
    arr[i], arr[r - 1] = arr[r - 1], arr[i]
    return partition(arr, p, r)
