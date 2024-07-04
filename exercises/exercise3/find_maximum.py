def find_maximum(x: list[int], low: int = 0, high: int | None = None) -> int:
    if high is None:
        high = len(x) - 1

    if high - low < 2:
        return max(x[low], x[high])

    mid = (low + high) // 2

    if x[low] > max(x[low - 1], x[low + 1]):
        return x[low]
    if x[low - 1] < x[low] < x[low + 1]:
        if x[mid] < x[mid + 1] and x[mid] > x[low]:
            return find_maximum(x, mid, high)
        return find_maximum(x, low, mid)
    if x[mid] < x[low] or x[mid] < x[mid + 1]:
        return find_maximum(x, mid, high)
    return find_maximum(x, low, mid)
