def counting_sort(arr: list[int], n: int, k: int) -> list[int]:
    b = []
    c = [0] * k
    for i in range(n):
        c[arr[i]] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        b[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1
    return b
