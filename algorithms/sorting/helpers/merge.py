def merge(arr: list[int], p: int, q: int, r: int) -> None:
    infinity = max(arr) + 1
    left = arr[p:q] + [infinity]
    right = arr[q:r] + [infinity]
    i = 0
    j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
