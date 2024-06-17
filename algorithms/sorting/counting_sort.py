def counting_sort(a: list[int], n: int, k: int) -> list[int]:
    b = []
    c = [0] * k

    for i in range(n):
        c[a[i]] += 1

    for i in range(1, k):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1

    return b
