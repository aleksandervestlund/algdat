import itertools


def bucket_sort(arr: list[int], n: int) -> list[int]:
    b = [[] for _ in range(n)]
    for i in range(n):
        x = arr[i]
        b[int(n * x)].append(x)
    for i in range(n):
        b[i] = sorted(b[i])
    return list(itertools.chain.from_iterable(b))
