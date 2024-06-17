def radix_sort(a: list[int], d: int) -> list[int]:
    for i in range(d):
        a = sorted(a, key=lambda x: x // 10**i % 10)

    return a


def xidar_non_sort(a: list[int], d: int) -> list[int]:
    for i in range(d, -1, -1):
        a = sorted(a, key=lambda x: x // 10**i % 10)

    return a
